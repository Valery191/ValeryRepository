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

### 📊 Test Coverage

| Module | Coverage | Status |
|--------|----------|--------|
| CRM Management | 85% | ✅ |
| Authentication | 90% | ✅ |
| Customer Management | 75% | ✅ |
| Pipeline Verification | 70% | ✅ |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git
- Chrome/Firefox browser (for local execution)

### Installation

```bash
# Clone the repository
git clone <your-repository-url>
cd crm_automation

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install browser drivers
python -m playwright install --with-deps
