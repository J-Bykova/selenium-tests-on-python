Feature: Validation of pages

  Scenario Outline: Search validation on few pages
    Given Main page is open
    When  I enter '<product>' into the search field
    And   I click the search button
    Then  I see '<product>' on first '<num>' pages
    Examples:
      | product | num |
      | Shoes   | 3   |


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
    Then  I see the words '<words>' in each result heading from '<from>' to '<to>'
    Examples:
      | words                           | from | to |
      | Shoe,Shoes,Sneakers,Trail,Asics | 1    | 3  |
      | Shoe,Shoes,Sneakers,Trail,Asics | 3    | 5  |
      | Shoe,Shoes,Sneakers,Trail,Asics | 5    | 3  |
