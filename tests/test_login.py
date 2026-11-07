import pytest

from config.config import Config
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utilities.test_data_loader import get_invalid_credentials


@pytest.mark.smoke
def test_valid_admin_login(driver):
    login = LoginPage(driver).open_page()
    login.login(Config.ADMIN_USER, Config.ADMIN_PASSWORD)

    dashboard = DashboardPage(driver)
    assert dashboard.is_opened(), "Dashboard did not open after login"


@pytest.mark.regression
@pytest.mark.parametrize("creds", get_invalid_credentials())
def test_invalid_login_shows_error(driver, creds):
    login = LoginPage(driver).open_page()
    login.login(creds["username"], creds["password"])

    assert login.is_error_displayed(), "Error message was not displayed"
    assert "invalid" in login.get_error_message().lower()


@pytest.mark.regression
def test_logout_returns_to_login(driver):
    LoginPage(driver).open_page().login(Config.ADMIN_USER, Config.ADMIN_PASSWORD)
    dashboard = DashboardPage(driver)
    assert dashboard.is_opened()

    dashboard.logout()
    assert "login" in driver.current_url.lower()


@pytest.mark.regression
def test_forgot_password_navigation(driver):
    login = LoginPage(driver).open_page()
    login.click_forgot_password()
    assert "reset" in driver.current_url.lower()
