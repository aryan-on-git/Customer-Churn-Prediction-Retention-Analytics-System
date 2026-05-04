# Contributing Guidelines

## Commit Message Format

All commits should follow this format for consistency:

```
[TYPE] Step X: Brief description

Optional longer description explaining the changes.

Examples:
- [SETUP] Step 1: Initialize project structure
- [DATA] Step 2: Add dataset and EDA notebook
- [FEATURE] Step 3: Implement feature engineering
- [ML-MODEL] Step 4: Train and evaluate models
- [API] Step 5: Develop Flask REST API
- [FRONTEND] Step 6: Build React dashboard
- [INTEGRATION] Step 7: Add setup and testing
- [DOCS] Step 8: Complete documentation
```

## Code Style

### Python
- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to functions and classes
- Use type hints where appropriate

### JavaScript/React
- Use functional components with hooks
- Use descriptive component names (PascalCase for components)
- Add JSDoc comments for complex logic
- Keep CSS organized by component

## Testing

- Write tests for new features
- Run existing tests before committing
- Maintain >80% code coverage for production code

## Pull Request Process

1. Create a feature branch: `git checkout -b feature/description`
2. Make your changes and commit with proper messages
3. Push to your fork
4. Create a Pull Request with clear description
5. Ensure all tests pass
6. Request review from maintainers

## Reporting Issues

When reporting issues, please include:
- Detailed description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Environment details (Python/Node version, OS)
- Error messages or logs

## Project Standards

### Code Quality
- Linting: ESLint for JS, Pylint for Python
- Formatting: Prettier for JS, Black for Python
- Testing: Jest for JS, Pytest for Python

### Documentation
- Maintain up-to-date README
- Document API changes in API_DOCUMENTATION.md
- Update INTEGRATION_GUIDE for setup changes
- Add comments for complex logic

### Version Control
- Use clear, atomic commits
- One feature per branch
- Rebase before merging
- Delete branches after merge

## Development Workflow

### Adding a Feature

1. **Plan**: Describe changes and impact
2. **Code**: Implement with tests
3. **Test**: Verify locally and in CI
4. **Document**: Update relevant docs
5. **Commit**: Use proper commit format
6. **Review**: Address feedback
7. **Merge**: Integrate to main branch

### Fixing a Bug

1. Create issue describing the bug
2. Create branch: `git checkout -b fix/issue-description`
3. Write failing test first
4. Fix the bug
5. Verify test passes
6. Commit and create PR

## Local Development Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r backend/requirements.txt
pip install pytest black pylint

# Install frontend dev dependencies
cd frontend
npm install --save-dev

# Run tests before committing
pytest backend/
npm test
```

## Questions?

- Check documentation in INTEGRATION_GUIDE.md
- Review existing commits for examples
- Open a discussion issue if unsure

Thank you for contributing!
