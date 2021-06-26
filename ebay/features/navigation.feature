Feature: Navigation menu
  Scenario: The 'Sign in' link leads to the 'Sign in or Register' page
      Given Main page is open
      When  I click the 'Sign in' link in the top header
      Then  I see the 'Sign in or Register | eBay' page
