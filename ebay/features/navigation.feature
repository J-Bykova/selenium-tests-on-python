Feature: Navigation menu
  Scenario: The 'Sign in' link leads to the 'Sign in or Register' page
      Given Main page is open
      When  I click the 'Sign in' link in the top header
      Then  I see the 'Sign in or Register | eBay' page


  Scenario: The 'register' link leads to the 'Register: Create a personal account' page
    Given Main page is open
    When  I click the 'register' link in the top header
    Then  I see the 'Register: Create a personal account' page


  Scenario: The 'Daily Deals' link leads to the 'Daily Deals on eBay | Best deals and Free Shipping' page
    Given Main page is open
    When  I click the 'Daily Deals' link in the top header
    Then  I see the 'Daily Deals on eBay | Best deals and Free Shipping' page


  Scenario: The 'Brand Outlet' link leads to the 'Brand Outlet products for sale | eBay' page
    Given Main page is open
    When  I click the 'Brand Outlet' link in the top header
    Then  I see the 'Brand Outlet products for sale | eBay' page


  Scenario: The 'Help & Contact' link leads to the 'eBay Customer Service' page
    Given Main page is open
    When  I click the 'Help & Contact' link in the top header
    Then  I see the 'eBay Customer Service' page


  Scenario: The 'Sell' link leads to the 'Selling on eBay | Electronics, Fashion, Home & Garden | eBay' page
    Given Main page is open
    When  I click the 'Sell' link in the top header
    Then  I see the 'Selling on eBay | Electronics, Fashion, Home & Garden | eBay' page