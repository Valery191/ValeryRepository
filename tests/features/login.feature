Feature: User authentication

  Scenario: Successful login with valid credentials
    Given the user is on the login page
    When the user logs in with valid credentials
    Then the dashboard should be displayed

  Scenario: Login with invalid password
    Given the user is on the login page
    When the user logs in with an invalid password
    Then an error message should be shown
