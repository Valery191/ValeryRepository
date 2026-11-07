# CRM Automation Test Framework

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/selenium-4.15.0-green.svg)](https://www.selenium.dev/)
[![pytest](https://img.shields.io/badge/pytest-7.4.3-orange.svg)](https://docs.pytest.org/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## 📋 Overview

CRM Automation Test Framework is a comprehensive test automation solution for web-based CRM applications. Built with Python and Selenium WebDriver, it implements the Page Object Model (POM) design pattern to ensure maintainable, scalable, and reliable test automation.

### 🎯 Key Features

- **Page Object Model Architecture** - Clean separation of test logic and page elements
- **Comprehensive Test Coverage** - CRM module, authentication, and workflow testing
- **Parallel Execution** - Run tests in parallel for faster feedback
- **Rich Reporting** - HTML reports with screenshots on failure
- **CI/CD Ready** - Integration with GitHub Actions and other CI platforms
- **Data-Driven Testing** - Support for external test data sources
- **BDD Support** - Business-readable test scenarios with Gherkin

---

## 🚀 Quick Start

### Prerequisites

Before you begin, ensure you have the following installed:

*   **Python 3.8+** — [Download here](https://www.python.org/downloads/)
*   **Git** — [Download here](https://git-scm.com/)
*   **Chrome or Firefox** — for local execution
*   **pip** — comes pre-installed with Python

### Installation

**1. Clone the repository:**
```bash
git clone https://github.com/CRM/CRMRepository.git
cd CRMRepository
```

**2. Create and activate virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

**3. Install dependencies and browser drivers:**
```bash
pip install -r requirements.txt
python -m playwright install --with-deps
```

---
## 📂 Project structure
```text
crm_automation/
├── config/                 # Configuration and test data
├── pages/                  # Page Object Model classes
├── tests/                  # Test suites and BDD features
│   └── features/           # Gherkin scenarios
├── utilities/              # Driver factory, waits, logging, screenshots
├── reports/                # HTML reports and screenshots (generated)
├── .github/workflows/      # CI pipeline
├── .env.example            # Environment variables template
├── pytest.ini              # Pytest configuration
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

---
## Running Tests
```bash
# Full regression suite
pytest

# Smoke only
pytest -m smoke

# Specific module
pytest tests/test_customers.py

# Parallel execution
pytest -n 4

# With retries on flaky tests
pytest --reruns 2 --reruns-delay 1

# BDD scenarios
pytest tests/test_login_bdd.py
```
