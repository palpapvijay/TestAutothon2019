# Created by vijayago at 26-09-2019
Feature: TestAutothon problem solving scenario

  Scenario: Navigate to the Google.com and download photo's
    When search "step-in forum facebook"
    And click on results that contains text "25000 test professionals"
    And Navigate to the link fetched from the above step
    And Navigate to Posts
    And Find out the top post that has more than 4 photos.
    And Download top 5 photos in that post
    And Rename files in sequence
    And Validate size > 0 KB for each file
    Then files should be downloaded and renamed successfully

  Scenario: Extract Album's name and Photo counts.
    When Navigate to the Photo's and Click See All
    And Extract the album name and photo count for each album
    And Format the observation in JSON Format
    And Write to file named "data.json"
    Then data.json file should be created with album name and photo counts

  Scenario: Upload JSON file using HTTP details
    When Navigate to the data.json file file location
    And Upload it using HTTP details
    Then Verify file should be uploaded successfully