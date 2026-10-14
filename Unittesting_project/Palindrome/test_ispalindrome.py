import unittest

from isPalindrome import is_palindrome
class TestPalindrome(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_single_character(self):
        self.assertTrue(is_palindrome("a"))

    def test_mixed_case(self):
        self.assertTrue(is_palindrome("RaceCar"))

    def test_with_spaces_and_punctuation(self):
        self.assertTrue(
            is_palindrome("A man, a plan, a canal: Panama")
        )

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("hello"))
if __name__ == "__main__":
    unittest.main()
    