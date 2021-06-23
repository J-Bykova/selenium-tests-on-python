Feature: Page title
  Scenario: Check Google's title
    Given Browser is open
    When I go to 'http://google.com'
    Then I see the title is 'Google'

  Scenario Outline: Check many titles
    Given Browser is open
    When I go to '<url>'
    Then I see the title is '<title>'
    Examples:
      | url                 | title   |
      | http://youtube.com  | YouTube |
