Feature: Validation of pages

  Scenario Outline: Search validation on first 3 pages
    Given Main page is open
    When  I enter '<product>' into the search field
    And   I click the search button
    Then  I see '<product>' on first '<amount>' pages
    Examples:
      | product | amount |
      | Shoes   | 3      |


  Scenario Outline: Search validation on some pages
    Given Main page is open
    When  I enter 'Shoes' into the search field
    And   I click the search button
    And   I go to results page '<page>'
    Then  I see the word 'Shoes' in each result heading
    Examples:
      | page |
      | 3    |
      | 4    |
      | 5    |


  Scenario Outline: Search validation from X page to Y page
    Given Main page is open
    When  I enter 'Shoes' into the search field
    And   I click the search button
    And   I go to results page '<x_page>'
    Then  I see the word 'Shoes' in each result heading from '<x_page>' to '<y_page>'
    Examples:
      | x_page | y_page |
      | 1      | 2      |
      | 3      | 7      |
      | 6      | 2      |
