Feature: Field of Miracles
  Test Field of miracles to avoid mistakes
  Scenario: Generate word
    Given Generate word by seed 2
    When Print guess word
    Then Get printed guess word

  Scenario: Guess letter
    Given Guess letter ч
    When Check input letter
    Then print letter guess

  Scenario: Not guess letter
    Given Guess letter п
    When Check input letter
    Then print letter not guess

  Scenario: Not generated
    Given Guess letter а not generated
    When Check input letter not generated
    Then Print error