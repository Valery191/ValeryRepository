import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    BASE_URL = os.getenv("BASE_URL", "https://demo.crm-app.local")
    LOGIN_URL = f"{BASE_URL}/login"
    DASHBOARD_URL = f"{BASE_URL}/dashboard"

    BROWSER = os.getenv("BROWSER", "chrome")
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
    IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "5"))
    EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "15"))

    ADMIN_USER = os.getenv("ADMIN_USER", "admin@crm-app.local")
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "Admin123!")
    MANAGER_USER = os.getenv("MANAGER_USER", "manager@crm-app.local")
    MANAGER_PASSWORD = os.getenv("MANAGER_PASSWORD", "Manager123!")

    SCREENSHOT_DIR = os.getenv("SCREENSHOT_DIR", "reports/screenshots")
    REPORT_DIR = os.getenv("REPORT_DIR", "reports")
    TEST_DATA_DIR = os.getenv("TEST_DATA_DIR", "tests/test_data")
