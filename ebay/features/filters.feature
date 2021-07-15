Feature: Search by filters

Scenario Outline: Search for a valid product by 'Condition' filter
    Given Main page is open
    When  I enter '<product>' into the search field
    And   I click the search button
    And Click on checkbox '<option>' in '<filter>'
    Then I see selected '<option>'
    Examples:
    | product     | option           | filter     |
    | shoes       | New with tags    | Condition  |
