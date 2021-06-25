Feature: Ebay.com Regression test

  Scenario: Search field verification
      Given Open ebay
      And   I Search in field type Shoes
      Then  Click on the Search button
#      Then  Verify all items related to Shoes