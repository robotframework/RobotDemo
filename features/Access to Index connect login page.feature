Feature: Index connect lading page
  #First step is to open an browser
  Scenario: Open a browser
    When Browser is opened
    Then type in hsi.com.hk/IndexConnect
  
  Scenario: Login using dummy account
    When URL hsi.com.hk/IndexConnect is loaded
    Then locate the username field
    Then Input text "dummyuser1"
    Then input password "dummypassword" in password field
    
  