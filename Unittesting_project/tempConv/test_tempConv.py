import unittest

from tempConv import *

class TestTemperatureConverter(unittest.TestCase):

    def test_freezing_point(self):
        self.assertEqual(
            celsius_to_fahrenheit(0),
            32
        )

    def test_boiling_point(self):
        self.assertEqual(
            celsius_to_fahrenheit(100),
            212
        )

    def test_minus_40(self):
        self.assertEqual(
            celsius_to_fahrenheit(-40),
            -40
        )

    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(
            fahrenheit_to_celsius(212),
            100
        )

    def test_round_trip(self):
        original = 37.5

        converted = celsius_to_fahrenheit(original)

        result = fahrenheit_to_celsius(converted)

        self.assertAlmostEqual(
            original,
            result,
            places=6
        )

if __name__ == "__main__":
    unittest.main()
