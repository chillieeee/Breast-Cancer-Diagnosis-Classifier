# Contributing to Breast-Cancer-Diagnosis-Classifier

Thank you for considering contributing! This project follows a simple workflow to keep things tidy and maintain high quality.

## How to Contribute

1. **Fork the repository** on GitHub.
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/<your-username>/Breast-Cancer-Diagnosis-Classifier.git
   cd Breast-Cancer-Diagnosis-Classifier
   ```
3. **Create a virtual environment** and install the dependencies:
   ```bash
   python -m venv venv
   source venv/Scripts/activate   # Windows PowerShell
   pip install -r requirements.txt
   pip install -r dev-requirements.txt   # optional, see below
   ```
4. **Create a new branch** for your change:
   ```bash
   git checkout -b my-feature
   ```
5. **Make your changes**, ensuring code style is consistent (run the linters locally if you like).
6. **Run the test suite** to verify everything still works:
   ```bash
   pytest
   ```
7. **Commit and push** your changes:
   ```bash
   git add .
   git commit -m "Brief description of your change"
   git push origin my-feature
   ```
8. **Open a Pull Request** on the original repository and fill out the PR template.

## Code of Conduct

All participants are expected to follow the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). By participating, you agree to uphold a respectful and inclusive environment.

## Reporting Issues

If you encounter a bug or have a feature request, please open an issue on GitHub with a clear description and steps to reproduce.

## Development Dependencies (optional)

For contributors who want to run the CI locally, you can install the development tools with:
```bash
pip install ruff mypy pytest
```
These are listed in `dev-requirements.txt` (you may create it if needed).
