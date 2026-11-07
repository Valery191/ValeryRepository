from pytest_bdd import scenarios, given, when, then

from config.config import Config
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

scenarios("features/login.feature")


@given("the user is on the login page")
def on_login_page(driver):
    LoginPage(driver).open_page()


@when("the user logs in with valid credentials")
def login_valid(driver):
    LoginPage(driver).login(Config.ADMIN_USER, Config.ADMIN_PASSWORD)


@when("the user logs in with an invalid password")
def login_invalid(driver):
    LoginPage(driver).login(Config.ADMIN_USER, "wrong-password")


@then("the dashboard should be displayed")
def dashboard_displayed(driver):
    assert DashboardPage(driver).is_opened()


@then("an error message should be shown")
def error_shown(driver):
    assert LoginPage(driver).is_error_displayed()

@then("I cannot navigate back to the home page")
def verify_cannot_go_back(driver):
    driver.back()
    logout_page = LogoutPage(driver)
    assert logout_page.is_warning_message_displayed()
