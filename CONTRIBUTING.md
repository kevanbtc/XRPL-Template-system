# Contributing

Thanks for your interest in improving this project!

## Development setup

- Python 3.11+
- Optional: install PyYAML to enable YAML policy loading (the app falls back gracefully without it)

## Workflow

- Create a feature branch
- Make changes with tests or a minimal runtime check
- Run `python ai/run.py` to ensure the swarm completes and writes a run log
- Open a PR with a clear description; include policy changes if applicable

## Policy changes

- Update `ai/config/ai_policy.yaml`
- Note the change in your PR and route for approval

## Style

- Keep README sections lint‑friendly (headings and lists with blank lines)
- Avoid committing generated run logs (`output/ai_runs/*.json`)
