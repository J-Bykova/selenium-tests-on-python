Feature: Product search
  Scenario Outline: Search for a valid product type
      Given Main page is open
      When  I enter '<product>' into the search field
      And   I click the search button
      Then  I see the '<title>' page
      Examples:
        | product | title          |
        | phones  | phones \| eBay |
        | shoes   | shoes \| eBay  |
        | soap    | soap \| eBay   |