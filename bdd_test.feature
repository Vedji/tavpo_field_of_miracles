Feature: Field of Miracles
  Scenario: Generate word
    Given Generate word by seed 2
    When Print guess word
    Then Get printed guess word

  Scenario: Guess letter test
    Given Guess letter ч
    When Check input letter
    Then Print letter guess

  Scenario: Not guess letter
    Given Not Guess letter п
    When Not Check input letter
    Then Print letter not guess

  Scenario: Not generated
    Given Not generated Guess letter а
    When Check input letter not generated
    Then Print error