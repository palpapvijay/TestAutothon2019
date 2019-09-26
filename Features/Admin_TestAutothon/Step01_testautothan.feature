# Created by vijayago at 26-09-2019
Feature: TestAutothon problem solving scenario

  Scenario: Navigate to the Google.com and download photo's
    When search "step-in forum facebook"
    And click the google search button
    Then Navigate to the link fetched from the above step
