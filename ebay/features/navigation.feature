Feature: Navigation menu

  Scenario: The 'Sign in' link leads to the 'Sign in or Register' page
    Given Main page is open
    When  I click the 'Sign in' link in the top header
    Then  I see the 'Sign in or Register | eBay' page


  Scenario: The 'register' link leads to the 'Register: Create a personal account' page
    Given Main page is open
    When  I click the 'register' link in the top header
    Then  I see the 'Register: Create a personal account' page


  Scenario: The 'Watchlist' button open to the 'Please sign in to view items you are watching' drop-down window when user is not authorized
    Given Main page is open
    When  I click the 'Watchlist' link in the top header
    Then  I see the 'Please sign in to view items you are watching.' dropdown


  Scenario: The 'Sign in' link in Watchlist leads to the 'Sign in or Register' page
    Given Main page is open
    When  I click the 'Watchlist' link in the top header
    And   I click the 'Sign in' link in the Watchlist dropdown
    Then  I see the 'Sign in or Register | eBay' page


  Scenario Outline: The menu links in top header leads to the valid page
    Given Main page is open
    When  I click the '<name-link>' link in the top header
    Then  I see the '<title>' page
    Examples:
      | name-link      | title                                                          |
      | Daily Deals    | Daily Deals on eBay \| Best deals and Free Shipping            |
      | Brand Outlet   | Brand Outlet products for sale \| eBay                         |
      | Help & Contact | eBay Customer Service                                          |
      | Sell           | Selling on eBay \| Electronics, Fashion, Home & Garden \| eBay |
      | Expand My eBay | Sign in or Register \| eBay                                    |
