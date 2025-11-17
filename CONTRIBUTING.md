# Contributing

Thanks for your interest in improving this project! We welcome contributions of all kinds.

## Code of Conduct

This project adheres to a [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior via GitHub issues.

## Development Setup

### Prerequisites

- Python 3.11 or higher
- Git
- pip (Python package installer)

### Setting Up Your Development Environment

1. **Fork and clone the repository**

   ```bash
   git clone https://github.com/YOUR_USERNAME/XRPL-Template-system.git
   cd XRPL-Template-system
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv .venv
   
   # Activate on Windows
   .venv\Scripts\activate
   
   # Activate on macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   pip install -e ".[dev]"  # Install dev dependencies from pyproject.toml
   ```

4. **Install pre-commit hooks**

   ```bash
   pre-commit install
   ```

   This ensures code is automatically formatted and checked before each commit.

## Development Workflow

### Creating a Feature Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/issue-description
```

### Running Tests

Run the test suite to ensure everything works:

```bash
pytest
# or for verbose output
pytest -v
# or for a specific test file
pytest tests/test_config_policy_loading.py
```

### Code Formatting and Linting

This project uses several tools to maintain code quality:

- **black** - Code formatter
- **isort** - Import sorter
- **flake8** - Linter

Run these manually if needed:

```bash
# Format code
black .

# Sort imports
isort .

# Lint code
flake8 .

# Or run all checks via pre-commit
pre-commit run --all-files
```

### Running the AI Swarm

Test the main application:

```bash
python ai/run.py
```

This should complete successfully and write a run log to `output/ai_runs/`.

### Commit Message Guidelines

We follow conventional commit format for clear commit history:

- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `test:` - Test additions or modifications
- `refactor:` - Code refactoring
- `chore:` - Maintenance tasks
- `style:` - Code style changes (formatting, etc.)

Example:
```
feat: add new scoring dimension for asset liquidity
fix: correct policy loading when YAML file is missing
docs: update README with new installation steps
```

### Opening a Pull Request

1. Push your changes to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

2. Open a PR on GitHub with:
   - Clear title following commit message guidelines
   - Description of what changed and why
   - Reference any related issues (e.g., "Fixes #123")
   - Screenshots for UI changes (if applicable)

3. Ensure all CI checks pass

4. Address any review feedback

## Policy Changes

Changes to the AI policy require special attention:

1. Update `ai/config/ai_policy.yaml`
2. Document the change rationale in your PR description
3. Tag the PR with `policy-change` label
4. Request review from project maintainers for approval
5. Policy changes may require additional stakeholder approval

## Repository Structure

Understanding the codebase:

```
XRPL-Template-system/
├── ai/                      # AI swarm components
│   ├── src/
│   │   ├── agents/         # Agent implementations
│   │   ├── tools/          # Scoring and utility tools
│   │   └── swarm.py        # Core swarm orchestration
│   ├── config/             # Policy configuration
│   └── run.py              # Main entry point
├── scripts/                 # Scoring and indexing scripts
├── tests/                   # Test suite
├── docs/                    # Documentation and templates
├── data/                    # Input data (assets.json)
└── output/                  # Generated reports and logs
```

## Testing Guidelines

- Write tests for new features and bug fixes
- Maintain or improve test coverage
- Follow existing test patterns in `tests/`
- Use descriptive test names that explain what is being tested
- Keep tests focused and independent

## Documentation

- Update relevant documentation when making changes
- Add inline comments for complex logic
- Update README.md if user-facing features change
- Keep template documentation in `docs/templates/` current

## Style Guidelines

- Follow PEP 8 style guide (enforced by black and flake8)
- Keep README sections lint-friendly (headings and lists with blank lines)
- Use type hints where appropriate
- Write docstrings for public functions and classes
- Keep functions focused and modular

## What Not to Commit

- Generated run logs: `output/ai_runs/*.json`
- Virtual environment: `.venv/`
- IDE configuration: `.vscode/`, `.idea/`
- Cache files: `__pycache__/`, `.pytest_cache/`
- Sensitive data: API keys, credentials, personal data

The `.gitignore` file is configured to exclude these automatically.

## Getting Help

- Open an issue for bugs or feature requests
- Ask questions in pull request comments
- Check existing issues and documentation first

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
