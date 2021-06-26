Feature: Product search
  Scenario: Search for a valid product type
      Given Main page is open
      When  I enter 'Shoes' into the search field
      And   I click the search button
      Then  I see shoes in the search results
