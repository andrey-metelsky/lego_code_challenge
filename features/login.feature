@login
Feature: Login Functionality

  Scenario Outline: Login with valid credentials
    Given the user is on the login page
    When the user logs in as <username>
    Then the user is successfully logged in

    Examples:
      | username                |
      | STANDARD_USER           |
      | PERFORMANCE_GLITCH_USER |
      | PROBLEM_USER            |

  Scenario Outline: Login with invalid credentials
    Given the user is on the login page
    When the user logs in with invalid: <invalid_field>
    Then invalid credentials error message is displayed

    Examples:
      | invalid_field         |
      | username              |
      | password              |
      | username and password |

  Scenario: Login as locked user
    Given the user is on the login page
    When the user logs in as LOCKED_USER
    Then locked user error message is displayed

