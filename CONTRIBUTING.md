# Contributing

Thanks for your interest in improving this project! We welcome contributions from the community.

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

## Development Setup

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Git

### Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/kevanbtc/XRPL-Template-system.git
   cd XRPL-Template-system
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install black isort flake8 pytest pre-commit
   ```

4. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

## Development Workflow

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Write clean, readable code
   - Add tests for new functionality
   - Update documentation as needed

3. **Run linting and formatting**
   ```bash
   black ai/ scripts/ tests/
   isort ai/ scripts/ tests/
   flake8 ai/ scripts/ tests/
   ```

4. **Run tests**
   ```bash
   pytest
   ```

5. **Verify AI swarm dry-run**
   ```bash
   python ai/run.py
   ```

6. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: description of your changes"
   ```

7. **Push and create a PR**
   ```bash
   git push origin feature/your-feature-name
   ```

## Commit Message Guidelines

We follow [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `chore:` - Maintenance tasks
- `test:` - Adding or updating tests
- `refactor:` - Code refactoring

## Policy Changes

Policy changes require special attention:

- Update `ai/config/ai_policy.yaml`
- Note the change clearly in your PR description
- Explain the rationale and impact
- Route for approval from maintainers

## Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide
- Use [Black](https://github.com/psf/black) for code formatting
- Use [isort](https://pycqa.github.io/isort/) for import sorting
- Maximum line length: 88 characters
- Keep README sections lint-friendly (headings and lists with blank lines)

## Testing

- Write tests for new features
- Ensure all tests pass before submitting PR
- Aim for good test coverage
- Tests should be clear and maintainable

## What Not to Commit

- Generated run logs (`output/ai_runs/*.json`)
- Virtual environment directories (`.venv/`, `venv/`)
- IDE-specific files (`.vscode/`, `.idea/`)
- Compiled Python files (`__pycache__/`, `*.pyc`)

## Pull Request Process

1. Update the README.md with details of changes if applicable
2. Update the CHANGELOG.md following the existing format
3. Ensure CI checks pass
4. Request review from maintainers
5. Address any feedback
6. Once approved, your PR will be merged

## Questions?

Feel free to open an issue for questions or discussions about contributions.
