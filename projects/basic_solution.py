class Creature:
    def __init__(self, name, food_level=0):
        self.name = name
        self.food_level = food_level

    def needs_food(self):
        raise NotImplementedError(
            "Subclasses must implement the needs_food method"
        )

    def absorb_food(self, food_amount):
        raise NotImplementedError(
            "Subclasses must implement the absorb_food method"
        )

    def __str__(self):
        if self.needs_food():
            return f"The {self.name} needs food"

        return f"The {self.name} doesn't need food"


class Fish(Creature):

    FOOD_THRESHOLD = 10
    ABSORPTION_RATE = 0.60

    def needs_food(self):
        return self.food_level < self.FOOD_THRESHOLD

    def absorb_food(self, food_amount):
        absorbed_amount = food_amount * self.ABSORPTION_RATE
        self.food_level += absorbed_amount


class Plant(Creature):

    FOOD_THRESHOLD = 15
    ABSORPTION_RATE = 0.50

    def needs_food(self):
        return self.food_level < self.FOOD_THRESHOLD

    def absorb_food(self, food_amount):
        absorbed_amount = food_amount * self.ABSORPTION_RATE
        self.food_level += absorbed_amount


class Aquarium:

    def __init__(self):
        self.creatures = []

    def add_creature(self, creature):
        self.creatures.append(creature)

    def feed(self, total_food):
        hungry_creatures = [
            creature
            for creature in self.creatures
            if creature.needs_food()
        ]

        if not hungry_creatures:
            print("No creatures need food")
            return

        food_per_creature = total_food / len(hungry_creatures)

        for creature in hungry_creatures:
            creature.absorb_food(food_per_creature)

    def display_state(self):
        for creature in self.creatures:
            print(creature)


def main():
    aquarium = Aquarium()

    aquarium.add_creature(Fish("goldfish"))
    aquarium.add_creature(Fish("clownfish"))
    aquarium.add_creature(Plant("seaweed"))
    aquarium.add_creature(Plant("kelp"))

    print("Before feeding:")
    aquarium.display_state()

    print("\nAfter feeding with 50:")
    print("Feeding with 50")
    aquarium.feed(50)
    aquarium.display_state()

    print("\nAfter feeding with 80:")
    print("Feeding with 80")
    aquarium.feed(80)
    aquarium.display_state()


if __name__ == "__main__":
    main()