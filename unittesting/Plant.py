from Creature import Creature

class Plant(Creature):
    def __init__(self, name, food_level):
        super().__init__(name, food_level, needs_food_below=15, absorbs=50)
    