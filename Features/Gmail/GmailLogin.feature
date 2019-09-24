# Created by apollu at 23-09-2019
  @gmail
Feature: Login Gmail Account

  Scenario: Login with Gmail Credentials
    When user enters valid gmail username
    And user clicks next button
    And user enters valid gmail password
    And user clicks next button
    Then user should be logged in successfully

    


