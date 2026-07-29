# features/login.feature
"""
Feature: Login and Logout
  As a user
  I want to login and logout of the application
  So that I can access protected features

  Scenario: Successful login
    Given I am on the login page
    When I enter valid credentials
    And I click the login button
    Then I should be redirected to the dashboard

  Scenario: Successful logout
    Given I am logged in
    When I click the user menu
    And I click the logout option
    Then I should see the login dashboard
    And I cannot navigate back to the home page
"""

# tests/step_defs/test_login_steps.py
from pytest_bdd import given, when, then, scenario
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from config.config import Config

@scenario("features/login.feature", "Successful login")
def test_successful_login():
    pass

@scenario("features/login.feature", "Successful logout")
def test_successful_logout():
    pass

@given("I am on the login page")
def go_to_login_page(driver):
    driver.get(Config.BASE_URL)
    return LoginPage(driver)

@when("I enter valid credentials")
def enter_valid_credentials(driver):
    login_page = LoginPage(driver)
    login_page.login(Config.VALID_EMAIL, Config.VALID_PASSWORD)

@when("I click the login button")
def click_login(driver):
    # Already handled in login method
    pass

@then("I should be redirected to the dashboard")
def verify_dashboard(driver):
    assert "dashboard" in driver.current_url.lower()

@given("I am logged in")
def login_user(driver):
    login_page = LoginPage(driver)
    login_page.login(Config.VALID_EMAIL, Config.VALID_PASSWORD)

@when("I click the user menu")
def click_user_menu(driver):
    logout_page = LogoutPage(driver)
    logout_page.click_user_menu()

@when("I click the logout option")
def click_logout(driver):
    logout_page = LogoutPage(driver)
    logout_page.click_logout()

@then("I should see the login dashboard")
def verify_login_dashboard(driver):
    logout_page = LogoutPage(driver)
    expected_title = "Login | Best solution for startups"
    assert logout_page.is_logout_successful(expected_title)

@then("I cannot navigate back to the home page")
def verify_cannot_go_back(driver):
    driver.back()
    logout_page = LogoutPage(driver)
    assert logout_page.is_warning_message_displayed()
