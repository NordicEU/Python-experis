import unittest

from passwordValid import validate_password

class TestPasswordValidator(unittest.TestCase):

    def test_valid_password(self):
        self.assertTrue(
            validate_password("Password1!")
        )

    def test_too_short(self):
        self.assertFalse(
            validate_password("Aa1!")
        )

    def test_missing_uppercase(self):
        self.assertFalse(
            validate_password("password1!")
        )

    def test_missing_lowercase(self):
        self.assertFalse(
            validate_password("PASSWORD1!")
        )

    def test_missing_digit(self):
        self.assertFalse(
            validate_password("Password!")
        )

    def test_missing_special_character(self):
        self.assertFalse(
            validate_password("Password1")
        )

if __name__ == "__main__":
    unittest.main()