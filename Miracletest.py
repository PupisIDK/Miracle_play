import unittest
from zaza import play_game


class TestGame(unittest.TestCase):

    # Tigran
    def test_valid_num_players(self):
        game = play_game()
        game.start(num_players=2)
        self.assertEqual(game.num_players, 2)

    def test_invalid_num_players(self):
        with self.assertRaises(ValueError):
            game = play_game()
            game.start(num_players=5)

    # Oleg
    def test_pick_word(self):
        game = play_game()
        word = game.pick_word()
        self.assertIn(word, game.words)

    def test_hide_word(self):
        game = play_game()
        hidden = game.hide_word("python")
        self.assertEqual(hidden, "******")


if __name__ == '__zaza__':
    unittest.zaza()