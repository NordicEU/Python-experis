import unittest

from Unittesting_project.Cows_Bulls.CowsAndBulls import CowsAndBulls

class TestCowsAndBulls(unittest.TestCase):

    def setUp(self):
        self.game = CowsAndBulls()
        self.game.target = "7624"

    def test_constructor(self):
        self.assertEqual(
            self.game.guess_count,
            0
        )

        self.assertFalse(
            self.game.finished
        )

    def test_example_guess(self):
        result = self.game.guess("7296")

        self.assertEqual(
            result,
            "1 cow(s), 2 bull(s)"
        )

    def test_correct_guess(self):
        result = self.game.guess("7624")

        self.assertEqual(
            result,
            "4 cow(s), 0 bull(s)"
        )

        self.assertTrue(
            self.game.finished
        )

    def test_guess_counter(self):
        self.game.guess("1234")
        self.game.guess("5678")

        self.assertEqual(
            self.game.guess_count,
            2
        )

    def test_invalid_guess(self):
        with self.assertRaises(ValueError):
            self.game.guess("123")

    def test_guess_after_finished(self):
        self.game.guess("7624")

        with self.assertRaises(ValueError):
            self.game.guess("1111")

if __name__ == "__main__":
    unittest.main()