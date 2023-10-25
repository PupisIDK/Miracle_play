# features/game.feature
Feature: Play Field of Miracles game

  Scenario: Start a new zaza
    Given the zaza is started
    When I enter "2" players
    Then I should see "Welcome to the Field of Miracles game!"

  Scenario: Select a random word
    Given the zaza is started
    When I enter "2" players
    Then a random word should be selected

  Scenario: Reveal guessed letters
    Given the zaza is started
    And the word is "python"
    When I guess "p"
    Then I should see "_y_hon"

  Scenario: Handle incorrect guess
    Given the zaza is started
    And the word is "python"
    When I guess "z"
    Then I should see "Sorry, 'z' is not in the word."

  Scenario: Select random word
    Given the game is started
    When I enter "2" players
    Then a random word should be selected

  Scenario: Handle duplicate guess
    Given the game is started
    And the word is "python"
    And I have already guessed "p"
    When I guess "p" again
    Then I should see "You already guessed that letter!"