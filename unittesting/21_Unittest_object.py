import unittest

from Fish import Fish
from Plant import Plant

class TestAquarium(unittest.TestCase):
    def test_goldfish(self):
        # Arrange
        goldfish = Fish("Goldfish", 0)
        # Act
        goldfish.update_food_level(20)
        # Assert
        self.assertEqual(goldfish.food_level, 12, f"Expected food level to be 12, but got {goldfish.food_level}")

    def test_seeweed(self):
        # Arrange
        seaweed = Plant("Seaweed", 0)
        # Act
        seaweed.update_food_level(16)
        # Assert
        self.assertEqual(seaweed.food_level, 8, f"Expected food level to be 8, but got {seaweed.food_level}")

if __name__ == '__main__':
    unittest.main()