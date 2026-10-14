import unittest

from fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):

    def test_one(self):
        self.assertEqual(
            fizzbuzz(1),
            ["1"]
        )

    def test_five(self):
        self.assertEqual(
            fizzbuzz(5),
            ["1", "2", "Fizz", "4", "Buzz"]
        )

    def test_fifteen(self):
        self.assertEqual(
            fizzbuzz(15)[-1],
            "FizzBuzz"
        )

    def test_zero(self):
        with self.assertRaises(ValueError):
            fizzbuzz(0)

    def test_negative(self):
        with self.assertRaises(ValueError):
            fizzbuzz(-5)

    def test_non_integer(self):
        with self.assertRaises(ValueError):
            fizzbuzz(3.5)

if __name__ == "__main__":
    unittest.main()