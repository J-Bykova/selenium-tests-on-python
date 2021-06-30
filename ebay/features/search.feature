Feature: Product search

  Scenario Outline: Search for a valid product type by search input
    Given Main page is open
    When  I enter '<product>' into the search field
    And   I click the search button
    Then  I see the '<title>' page
    Examples:
      | product | title          |
      | phones  | phones \| eBay |
      | shoes   | shoes \| eBay  |
      | soap    | soap \| eBay   |


  Scenario Outline: Search for a valid product type by 'Shop by category' button
    Given Main page is open
    When  I click the 'Shop by category' button
    And I click the '<product_category>' link
    Then  I see the '<title>' page
    Examples:
      | product_category          | title                                                                 |
      | Cell phones & accessories | Cell Phones, Smartphones, Smart Watches & Accessories for Sale - eBay |
      | Yard, garden & outdoor    | Yard, Garden & Outdoor Living Items for sale \| In Stock \| eBay      |
      | Motorcycles               | Motorcycles for sale \| eBay                                          |


  Scenario Outline: Search for a valid product type by 'All Categories' dropdown
    Given Main page is open
    When I click the 'All Categories' dropdown
    And I push the '<category>' link
    And  I click the search button
    Then  I see the '<title>' page
    Examples:
      | category              | title                                           |
      | Music                 | Music for sale \| eBay                          |
      | Dolls & Bears         | Dolls & Teddy Bears for sale \| eBay            |
      | Tickets & Experiences | Tickets & Experiences products for sale \| eBay |