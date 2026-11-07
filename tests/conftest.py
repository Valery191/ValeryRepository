import os
import pytest

from utilities.driver import DriverFactory
from utilities.screenshot import take_screenshot
from pages.login_page import LoginPage
from config.config import Config


@pytest.fixture(scope="session", autouse=True)
def setup_dirs():
    os.makedirs(Config.REPORT_DIR, exist_ok=True)
    os.makedirs(Config.SCREENSHOT_DIR, exist_ok=True)


@pytest.fixture(scope="function")
def driver(request):
    drv = DriverFactory.get_driver()
    drv.delete_all_cookies()

    yield drv

    if request.node.rep_call.failed:
        take_screenshot(drv, request.node.name)

    drv.quit()


@pytest.fixture(scope="function")
def logged_in_driver(driver):
    login = LoginPage(driver).open_page()
    login.login(Config.ADMIN_USER, Config.ADMIN_PASSWORD)
    yield driver


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
