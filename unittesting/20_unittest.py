import unittest
from Math import *

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        result = add(1, 2)
        self.assertEqual(result, 3, f"Expected 3, but got {result}")

    def test_subtract(self):
        result = subtract(5, 3)
        self.assertEqual(result, 2, f"Expected 2, but got {result}")

    def test_multiply(self):
        result = multiply(4, 5)
        self.assertEqual(result, 20, f"Expected 20, but got {result}")

    def test_divide(self):
        self.assertRaises(ValueError, divide, 10, 0)

if __name__ == '__main__':
    unittest.main()