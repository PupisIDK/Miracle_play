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

