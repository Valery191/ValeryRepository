# ValeryRepository

# Run all login/logout tests
pytest tests/test_login_logout.py -v

# Run specific test
pytest tests/test_login_logout.py::TestLoginLogout::test_successful_login -v

# Run with HTML report
pytest tests/test_login_logout.py --html=reports/login_report.html

# Run with environment variables
VALID_EMAIL=user@example.com VALID_PASSWORD=password123 pytest tests/test_login_logout.py

# Run BDD tests
pytest tests/step_defs/ -v
