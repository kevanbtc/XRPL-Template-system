# XRPL Private Cluster Setup Guide

**Document Version:** 1.0
**Last Updated:** 2025-11-16
**Purpose:** Step-by-step instructions for deploying XRPL-P (private ledger)
**Difficulty:** Intermediate to Advanced
**Time:** 4-6 hours for initial setup

---

## Prerequisites

### Required Knowledge
- Basic Linux system administration
- AWS EC2 management
- VPC/subnet/security group concepts
- Command-line tools (ssh, bash, systemd)
- rippled configuration basics

### Required Resources
- AWS account with EC2 permissions
- 2-5 EC2 instances (t3.large minimum, t3.xlarge recommended)
- Existing VPC or ability to create one
- Private subnet (or dedicated CIDR block)
- S3 bucket for configuration backups (optional)

### Software
- rippled (latest stable) – will be installed on each node
- AWS CLI configured locally
- SSH client
- Text editor (vim, nano, or local editor)

---

## Part 1: Network Architecture Planning

### Design Decision Matrix

**Question 1: How many validators?**
- **1 validator:** Fastest to set up, but single point of failure (dev/testing only)
- **3 validators:** Good for production, 2/3 threshold
- **5 validators:** High availability, 3/5 threshold (recommended for production)

**Question 2: Separate VPC or shared?**
- **Separate VPC:** Maximum isolation, no accidental public exposure
- **Shared VPC with private subnet:** Easier integration with existing infrastructure

**Question 3: Stock nodes?**
- **Minimum 1:** For API access to ledger
- **Recommended 2-3:** Load balancing, high availability for applications

### Reference Architecture (3 Validators + 2 Stock Nodes)

```
VPC: 10.0.0.0/16

Private Subnet: 10.0.20.0/24
├── Validator-1:   10.0.20.10
├── Validator-2:   10.0.20.11
├── Validator-3:   10.0.20.12
├── Stock-Node-1:  10.0.20.20
└── Stock-Node-2:  10.0.20.21

Bastion/VPN Subnet: 10.0.1.0/24
└── Bastion Host:  10.0.1.10 (SSH gateway)

Application Subnet: 10.0.30.0/24
└── Neural Relay:  10.0.30.10 (connects to stock nodes)
```

---

## Part 2: AWS Infrastructure Setup

### Step 1: Create VPC and Subnets

**Option A: Using AWS Console**
1. Navigate to VPC Dashboard
2. Create VPC: `xrpl-private-vpc` (10.0.0.0/16)
3. Create subnets:
   - `xrpl-private-validators` (10.0.20.0/24)
   - `xrpl-private-bastion` (10.0.1.0/24)
   - `xrpl-private-apps` (10.0.30.0/24)
4. Create Internet Gateway (for bastion only)
5. Create NAT Gateway (for outbound updates)

**Option B: Using Terraform** (recommended for repeatability)

Create `xrpl-private-infra.tf`:

```hcl
# VPC
resource "aws_vpc" "xrpl_private" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name = "xrpl-private-vpc"
    Environment = "production"
  }
}

# Private Subnet for Validators
resource "aws_subnet" "validators" {
  vpc_id            = aws_vpc.xrpl_private.id
  cidr_block        = "10.0.20.0/24"
  availability_zone = "us-east-1a"

  tags = {
    Name = "xrpl-private-validators"
  }
}

# Bastion Subnet
resource "aws_subnet" "bastion" {
  vpc_id                  = aws_vpc.xrpl_private.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "us-east-1a"
  map_public_ip_on_launch = true

  tags = {
    Name = "xrpl-private-bastion"
  }
}

# Application Subnet
resource "aws_subnet" "apps" {
  vpc_id            = aws_vpc.xrpl_private.id
  cidr_block        = "10.0.30.0/24"
  availability_zone = "us-east-1a"

  tags = {
    Name = "xrpl-private-apps"
  }
}

# Internet Gateway (bastion access)
resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.xrpl_private.id

  tags = {
    Name = "xrpl-private-igw"
  }
}

# NAT Gateway (for validator updates)
resource "aws_eip" "nat" {
  domain = "vpc"
}

resource "aws_nat_gateway" "main" {
  allocation_id = aws_eip.nat.id
  subnet_id     = aws_subnet.bastion.id

  tags = {
    Name = "xrpl-private-nat"
  }
}

# Route Tables
resource "aws_route_table" "public" {
  vpc_id = aws_vpc.xrpl_private.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main.id
  }

  tags = {
    Name = "xrpl-private-public-rt"
  }
}

resource "aws_route_table" "private" {
  vpc_id = aws_vpc.xrpl_private.id

  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.main.id
  }

  tags = {
    Name = "xrpl-private-private-rt"
  }
}

# Route Table Associations
resource "aws_route_table_association" "bastion" {
  subnet_id      = aws_subnet.bastion.id
  route_table_id = aws_route_table.public.id
}

resource "aws_route_table_association" "validators" {
  subnet_id      = aws_subnet.validators.id
  route_table_id = aws_route_table.private.id
}

resource "aws_route_table_association" "apps" {
  subnet_id      = aws_subnet.apps.id
  route_table_id = aws_route_table.private.id
}
```

**Apply:**
```bash
terraform init
terraform plan
terraform apply
```

### Step 2: Create Security Groups

**Validator Security Group:**

```hcl
resource "aws_security_group" "xrpl_validator" {
  name        = "xrpl-private-validator-sg"
  description = "XRPL Private Validator Security Group"
  vpc_id      = aws_vpc.xrpl_private.id

  # Peer protocol (between validators)
  ingress {
    description = "XRPL Peer Protocol"
    from_port   = 51235
    to_port     = 51235
    protocol    = "tcp"
    cidr_blocks = ["10.0.20.0/24"]
  }

  # JSON-RPC (from apps and bastion only)
  ingress {
    description = "XRPL JSON-RPC"
    from_port   = 5005
    to_port     = 5005
    protocol    = "tcp"
    cidr_blocks = ["10.0.30.0/24", "10.0.1.0/24"]
  }

  # WebSocket (from apps and bastion only)
  ingress {
    description = "XRPL WebSocket"
    from_port   = 6006
    to_port     = 6006
    protocol    = "tcp"
    cidr_blocks = ["10.0.30.0/24", "10.0.1.0/24"]
  }

  # SSH (from bastion only)
  ingress {
    description = "SSH from Bastion"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["10.0.1.0/24"]
  }

  # Outbound (for updates, NTP, etc.)
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "xrpl-private-validator-sg"
  }
}
```

**Bastion Security Group:**

```hcl
resource "aws_security_group" "bastion" {
  name        = "xrpl-private-bastion-sg"
  description = "Bastion Host Security Group"
  vpc_id      = aws_vpc.xrpl_private.id

  # SSH from your IP only (replace with your IP)
  ingress {
    description = "SSH from Admin"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["YOUR.IP.ADDRESS/32"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "xrpl-private-bastion-sg"
  }
}
```

### Step 3: Launch EC2 Instances

**Instance Specs:**
- **Validators:** t3.large (2 vCPU, 8GB RAM, 100GB gp3 SSD)
- **Stock Nodes:** t3.large (same, can scale up if high API load)
- **Bastion:** t3.micro (minimal)

**Launch Template (for validators):**

```hcl
resource "aws_launch_template" "xrpl_validator" {
  name_prefix   = "xrpl-private-validator-"
  image_id      = "ami-0c55b159cbfafe1f0"  # Ubuntu 22.04 LTS (update to current AMI)
  instance_type = "t3.large"

  key_name = aws_key_pair.xrpl_key.key_name

  network_interfaces {
    associate_public_ip_address = false
    security_groups             = [aws_security_group.xrpl_validator.id]
    subnet_id                   = aws_subnet.validators.id
  }

  block_device_mappings {
    device_name = "/dev/sda1"

    ebs {
      volume_size = 100
      volume_type = "gp3"
      iops        = 3000
      throughput  = 125
    }
  }

  tag_specifications {
    resource_type = "instance"

    tags = {
      Name = "xrpl-private-validator"
      Role = "validator"
    }
  }
}

# Launch 3 validators
resource "aws_instance" "validator" {
  count = 3

  launch_template {
    id      = aws_launch_template.xrpl_validator.id
    version = "$Latest"
  }

  private_ip = "10.0.20.${10 + count.index}"

  tags = {
    Name = "xrpl-private-validator-${count.index + 1}"
  }
}

# Launch 2 stock nodes (similar config, different IPs)
resource "aws_instance" "stock_node" {
  count = 2

  launch_template {
    id      = aws_launch_template.xrpl_validator.id
    version = "$Latest"
  }

  private_ip = "10.0.20.${20 + count.index}"

  tags = {
    Name = "xrpl-private-stock-node-${count.index + 1}"
    Role = "stock-node"
  }
}
```

---

## Part 3: rippled Installation

### On Each Node (Validator + Stock Nodes)

**SSH to bastion, then to each validator:**
```bash
# From local machine
ssh -i xrpl-key.pem ubuntu@<bastion-public-ip>

# From bastion
ssh ubuntu@10.0.20.10  # Validator-1
```

**Install rippled:**

```bash
# Update system
sudo apt-get update
sudo apt-get upgrade -y

# Install dependencies
sudo apt-get install -y wget gnupg2

# Add Ripple repository
wget -qO- https://repos.ripple.com/repos/rippled-deb/repo_key.asc | sudo apt-key add -
echo "deb https://repos.ripple.com/repos/rippled-deb/ focal stable" | sudo tee /etc/apt/sources.list.d/ripple.list

# Install rippled
sudo apt-get update
sudo apt-get install -y rippled

# Verify installation
rippled --version
# Should output: rippled-1.12.0+<build>
```

**Create rippled user (already done by package):**
```bash
# Verify rippled user exists
id rippled
# uid=999(rippled) gid=999(rippled) groups=999(rippled)
```

---

## Part 4: Validator Key Generation

### On Each Validator Node

**Generate validation keys:**

```bash
# Generate keys
rippled validation_create

# Output:
# {
#    "status" : "success",
#    "validation_key" : "FOLD TINT TWIN ABLE ..."
#    "validation_public_key" : "n9KorY8QtTdRx7TVDpw..."
#    "validation_seed" : "snoPBrXtMeMyMHUVTgb..."
# }
```

**CRITICAL: Store these securely!**

Create a secure storage file (local machine, not on servers):

`validator-keys.txt`:
```
Validator-1 (10.0.20.10):
  validation_public_key: n9KorY8QtTdRx7TVDpw...
  validation_seed: snoPBrXtMeMyMHUVTgb...

Validator-2 (10.0.20.11):
  validation_public_key: n9MzKz4X9rZr7TVDpw...
  validation_seed: ss5hK8rXtMeMyMHUVTgb...

Validator-3 (10.0.20.12):
  validation_public_key: n9LpQz8QtTdRx7TVDpw...
  validation_seed: shBtNrXtMeMyMHUVTgb...
```

**Encrypt and store in:**
- Password manager (1Password, Bitwarden)
- AWS Secrets Manager
- Hardware HSM (production)
- S3 bucket with KMS encryption

**Never commit to git, never store in plaintext on servers.**

---

## Part 5: rippled Configuration

### Validator Configuration

**On Validator-1 (10.0.20.10):**

```bash
sudo vim /etc/opt/ripple/rippled.cfg
```

**Configuration file:**

```ini
[server]
port_rpc_admin_local
port_peer
port_ws_admin_local

[port_rpc_admin_local]
port = 5005
ip = 0.0.0.0
admin = 10.0.30.0/24,10.0.1.0/24
protocol = http

[port_peer]
port = 51235
ip = 0.0.0.0
protocol = peer

[port_ws_admin_local]
port = 6006
ip = 0.0.0.0
admin = 10.0.30.0/24,10.0.1.0/24
protocol = ws

[node_size]
medium

[node_db]
type=NuDB
path=/var/lib/rippled/db/nudb
online_delete=2000
advisory_delete=0

[database_path]
/var/lib/rippled/db

[debug_logfile]
/var/log/rippled/debug.log

[sntp_servers]
time.windows.com
time.apple.com
time.nist.gov
pool.ntp.org

[ips_fixed]
10.0.20.11 51235
10.0.20.12 51235
10.0.20.20 51235
10.0.20.21 51235

[peer_private]
1

[validators_file]
validators.txt

[validation_seed]
snoPBrXtMeMyMHUVTgb...

[rpc_startup]
{ "command": "log_level", "severity": "info" }
```

**Key settings explained:**

- `peer_private = 1`: Only connect to specified peers, not public network
- `ips_fixed`: List of all other nodes (validators + stock nodes)
- `validation_seed`: THIS VALIDATOR'S seed (from generation step)
- `validators_file`: Points to validators.txt (next step)

**Repeat for Validator-2 and Validator-3:**
- Change `validation_seed` to each node's unique seed
- Keep `ips_fixed` identical (all nodes peer with all nodes)

### Stock Node Configuration

**On Stock-Node-1 (10.0.20.20):**

Same config as validators, BUT:
- **Remove `validation_seed` line** (stock nodes don't validate)
- **Remove `validators_file` line** (or keep for tracking)
- Keep `ips_fixed` pointing to validators

### Validators List File

**On each node, create `/etc/opt/ripple/validators.txt`:**

```
[validators]
n9KorY8QtTdRx7TVDpw...
n9MzKz4X9rZr7TVDpw...
n9LpQz8QtTdRx7TVDpw...

[validator_list_sites]

[validator_list_keys]
```

**Explanation:**
- `[validators]`: List all 3 (or 5) validator public keys
- No external validator sites (we're a closed network)
- This tells each node who to trust for ledger validation

---

## Part 6: Bootstrap and First Start

### Start in Standalone Mode (Validator-1 only)

**Purpose:** Generate genesis ledger

```bash
# On Validator-1
sudo systemctl stop rippled  # If already running

# Start in standalone
sudo -u rippled rippled --standalone &

# Wait for it to stabilise (20-30 seconds)
# Check status
rippled server_info

# You should see:
# "server_state": "standalone"
```

**Create genesis accounts (optional but recommended):**

```bash
# Generate a few master accounts
rippled wallet_propose

# Store these for future use (e.g., SPV accounts, issuer accounts)
```

**Stop standalone:**
```bash
# Find process
ps aux | grep rippled

# Kill gracefully
sudo kill <PID>
```

### Start Cluster Mode (All Nodes)

**On each node (Validator-1, 2, 3, Stock-1, 2):**

```bash
# Enable rippled service
sudo systemctl enable rippled

# Start rippled
sudo systemctl start rippled

# Check status
sudo systemctl status rippled
# Should show: active (running)

# Check logs
sudo tail -f /var/log/rippled/debug.log
```

**What to look for in logs:**

```
2025-Nov-16 12:00:00 Application:NFO Opened 'port_peer' (ip=0.0.0.0:51235, peer)
2025-Nov-16 12:00:01 Peer:NFO [001] onConnect: 10.0.20.11:51235
2025-Nov-16 12:00:02 Peer:NFO [002] onConnect: 10.0.20.12:51235
2025-Nov-16 12:00:05 LedgerConsensus:NFO Consensus built ledger #2
2025-Nov-16 12:00:09 LedgerConsensus:NFO Consensus built ledger #3
```

**Good signs:**
- Peers connecting (you should see 4 peer connections on each validator)
- Ledgers closing every 4-5 seconds
- "Consensus built ledger" messages

**Bad signs:**
- No peer connections → check `ips_fixed`, firewall, security groups
- "Waiting for ledger" stuck → validators not reaching quorum
- Errors about validation → check `validation_seed` and `validators.txt`

---

## Part 7: Verification and Testing

### Check Cluster Health

**On any node:**

```bash
# Server info
rippled server_info

# Look for:
# "server_state": "full" or "validating" (for validators)
# "complete_ledgers": "1-2000" (or similar range)
# "peers": 4 (validators see 4 others, stock nodes see 3 validators)

# Peer info
rippled peers

# Should list:
# 10.0.20.10:51235
# 10.0.20.11:51235
# 10.0.20.12:51235
# 10.0.20.20:51235 (if on validator)

# Validator list status
rippled validators

# Should show:
# Your 3 validator public keys
# "trusted": true
# "signing": true
```

### Test Basic Operations

**Create a test account:**

```bash
rippled wallet_propose
# Store address and secret

# Fund account (standalone genesis accounts should have XRP)
rippled submit '<funding_tx_blob>'
```

**Test API access from application subnet:**

```bash
# From your Neural Relay server (10.0.30.10)
curl -X POST http://10.0.20.20:5005 \
  -H "Content-Type: application/json" \
  -d '{
    "method": "server_info",
    "params": [{}]
  }'

# Should return JSON with server status
```

### Monitor Ledger Progression

```bash
# Watch ledgers close
watch -n 5 'rippled server_info | grep validated_ledger'

# Should increment every 4-5 seconds
# validated_ledger: 1523
# validated_ledger: 1524
# validated_ledger: 1525
```

---

## Part 8: Ongoing Operations

### Monitoring

**Key Metrics to Track:**

1. **Validator Health:**
   - All validators online: `systemctl status rippled`
   - Validation rate: check logs for "Consensus built ledger"
   - Peer connections: `rippled peers` (should always be 4)

2. **Ledger Progression:**
   - Ledgers closing every 4-5 seconds
   - No forks or disagreements
   - Consistent ledger hashes across all nodes

3. **Resource Usage:**
   - CPU: should be <50% average
   - RAM: 4-6GB per node
   - Disk: grows ~1-2GB/month
   - Network: minimal (private cluster, low tx volume)

**CloudWatch Alarms (recommended):**

```hcl
resource "aws_cloudwatch_metric_alarm" "validator_cpu" {
  alarm_name          = "xrpl-validator-high-cpu"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = "2"
  metric_name         = "CPUUtilization"
  namespace           = "AWS/EC2"
  period              = "300"
  statistic           = "Average"
  threshold           = "80"
  alarm_description   = "XRPL Validator CPU usage above 80%"
  alarm_actions       = [aws_sns_topic.alerts.arn]

  dimensions = {
    InstanceId = aws_instance.validator[0].id
  }
}
```

### Backups

**Database Backup:**

```bash
# On each node, daily cron job
0 2 * * * sudo tar -czf /backup/rippled-$(date +\%Y\%m\%d).tar.gz /var/lib/rippled/db
```

**Configuration Backup:**

```bash
# Store in S3
aws s3 cp /etc/opt/ripple/rippled.cfg s3://xrpl-private-configs/validator-1/rippled.cfg
aws s3 cp /etc/opt/ripple/validators.txt s3://xrpl-private-configs/validator-1/validators.txt
```

### Updates

**rippled Updates:**

```bash
# On each node, one at a time (don't take down quorum)

# 1. Update Validator-1
ssh ubuntu@10.0.20.10
sudo apt-get update
sudo apt-get install --only-upgrade rippled
sudo systemctl restart rippled

# Wait 5 minutes, verify healthy

# 2. Update Validator-2
ssh ubuntu@10.0.20.11
sudo apt-get install --only-upgrade rippled
sudo systemctl restart rippled

# Wait 5 minutes, verify healthy

# 3. Update Validator-3 (and stock nodes)
# ...
```

**Never update all validators simultaneously** → you'll lose quorum.

---

## Part 9: Integration with Neural Relay

### Connection Configuration

**In Neural Relay service:**

`config/xrpl.yaml`:
```yaml
xrpl:
  public:
    host: https://54.x.x.x:5005
    websocket: wss://54.x.x.x:6006
    network_id: 0
    timeout: 30
    retry_attempts: 3

  private:
    # Use stock node for reliability
    host: https://10.0.20.20:5005
    websocket: wss://10.0.20.20:6006
    network_id: 21337
    timeout: 30
    retry_attempts: 3
    failover_host: https://10.0.20.21:5005  # Stock-Node-2
```

### Load Balancing (Optional)

**For high-availability:**

Create internal ALB pointing to both stock nodes:

```hcl
resource "aws_lb" "xrpl_private" {
  name               = "xrpl-private-lb"
  internal           = true
  load_balancer_type = "application"
  security_groups    = [aws_security_group.xrpl_validator.id]
  subnets            = [aws_subnet.validators.id, aws_subnet.apps.id]
}

resource "aws_lb_target_group" "xrpl_private_http" {
  name     = "xrpl-private-http-tg"
  port     = 5005
  protocol = "HTTP"
  vpc_id   = aws_vpc.xrpl_private.id

  health_check {
    path                = "/"
    protocol            = "HTTP"
    matcher             = "200"
    interval            = 30
    timeout             = 10
    healthy_threshold   = 2
    unhealthy_threshold = 2
  }
}

resource "aws_lb_target_group_attachment" "stock_1" {
  target_group_arn = aws_lb_target_group.xrpl_private_http.arn
  target_id        = aws_instance.stock_node[0].id
  port             = 5005
}

resource "aws_lb_target_group_attachment" "stock_2" {
  target_group_arn = aws_lb_target_group.xrpl_private_http.arn
  target_id        = aws_instance.stock_node[1].id
  port             = 5005
}

resource "aws_lb_listener" "http" {
  load_balancer_arn = aws_lb.xrpl_private.arn
  port              = "5005"
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.xrpl_private_http.arn
  }
}
```

**Then in Neural Relay:**
```yaml
private:
  host: http://xrpl-private-lb-internal.us-east-1.elb.amazonaws.com:5005
```

---

## Part 10: Troubleshooting

### Common Issues

**Issue: Validators not connecting**

Check:
```bash
# Firewall rules
sudo iptables -L

# Security groups (AWS console or CLI)
aws ec2 describe-security-groups --group-ids sg-xxx

# rippled config ips_fixed
cat /etc/opt/ripple/rippled.cfg | grep -A5 ips_fixed
```

Fix:
- Ensure all IPs in `ips_fixed` are correct
- Verify security group allows 51235 from private subnet
- Check NAT gateway is working (validators need outbound for NTP)

**Issue: Ledgers not closing**

Check:
```bash
rippled validators

# Look for "signing": true on your validators
# If false → validation keys not loaded correctly
```

Fix:
- Verify `validation_seed` in rippled.cfg
- Ensure validators.txt has all public keys
- Restart rippled: `sudo systemctl restart rippled`

**Issue: High CPU usage**

Possible causes:
- Database corruption → restore from backup
- Too many API requests → add more stock nodes, use load balancer
- Memory issues → upgrade instance type

**Issue: Can't connect from application layer**

Check:
```bash
# From app server
telnet 10.0.20.20 5005

# Should connect
# If "Connection refused" → rippled not running or firewall issue
# If timeout → security group blocking
```

---

## Part 11: Production Hardening

### Security Best Practices

1. **Key Management:**
   - Store validator seeds in AWS Secrets Manager or HSM
   - Rotate seeds annually
   - Multi-sig for critical accounts

2. **Access Control:**
   - Bastion host with MFA
   - No direct SSH to validators (always via bastion)
   - VPN for admin access (instead of bastion)
   - Audit all SSH sessions (CloudTrail, Session Manager)

3. **Network Isolation:**
   - Private ledger never exposed to internet
   - Stock nodes only accessible from application subnet
   - Consider AWS PrivateLink for inter-VPC communication

4. **Monitoring:**
   - CloudWatch dashboards for all nodes
   - SNS alerts for validator downtime
   - Log aggregation (CloudWatch Logs or ELK stack)

### Disaster Recovery

**Backup Strategy:**
- Daily: Database snapshots to S3
- Weekly: Full AMI snapshots of all nodes
- Monthly: Test restore procedure

**Recovery Scenarios:**

**Single Validator Failure:**
1. Cluster continues (2/3 or 3/5 quorum maintained)
2. Launch replacement instance
3. Restore config from backup
4. Sync with network (automatic)
5. Re-enable validation

**Quorum Loss (2+ validators down):**
1. Network halts (no consensus)
2. Restore validators from AMI snapshots
3. If database corruption: restore last good backup
4. Restart all validators simultaneously
5. Network resumes from last validated ledger

**Total Cluster Loss:**
1. Restore all nodes from backups
2. If ledger history lost: start new genesis (all private data preserved if you have transaction logs)
3. Re-apply all transactions from application database

---

## Conclusion

You now have:

✅ **Private XRPL cluster** (3 validators, 2 stock nodes)
✅ **Network isolation** (private subnet, security groups)
✅ **High availability** (multi-validator consensus)
✅ **Operational procedures** (monitoring, backups, updates)
✅ **Application integration** (Neural Relay connection)

**Next Steps:**

1. Test vault NFT creation (Part 2 of Ruby Vault Template)
2. Build bridge logic between XRPL-M and XRPL-P
3. Deploy first RWA vault (Ruby Collection or test asset)
4. Integrate with Bank Filings page (proof bundles)

**Time Estimate:**
- Setup: 4-6 hours (if using Terraform)
- Testing: 2-3 hours
- Production hardening: 1-2 days
- Ongoing operations: <1 hour/week (monitoring + updates)

**Cost:**
- 5× t3.large instances: ~$300/month
- NAT Gateway: ~$30/month
- Data transfer: minimal (~$10/month)
- **Total: ~$340/month**

This is your **private ledger foundation** — the brain and conscience of your financial operating system.
