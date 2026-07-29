# ValeryRepository

# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest

# Run specific test
pytest tests/test_crm.py::TestCrm::test_create_opportunity

# Run with HTML report
pytest --html=reports/report.html

# Run in parallel
pytest -n 4
