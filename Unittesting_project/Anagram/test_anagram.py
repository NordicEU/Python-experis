import unittest
from anagram import are_anagrams


class TestAnagram(unittest.TestCase):

    def test_simple_anagram(self):
        self.assertTrue(
            are_anagrams("listen", "silent")
        )

    def test_case_insensitive(self):
        self.assertTrue(
            are_anagrams("Triangle", "Integral")
        )

    def test_with_spaces(self):
        self.assertTrue(
            are_anagrams("Dormitory", "Dirty Room")
        )

    def test_not_anagram(self):
        self.assertFalse(
            are_anagrams("hello", "world")
        )

    def test_different_lengths(self):
        self.assertFalse(
            are_anagrams("cat", "cats")
        )

if __name__ == "__main__":
    unittest.main()