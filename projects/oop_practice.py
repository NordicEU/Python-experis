class AquariumCreature:
    """The parent class for anything chilling in the aquarium."""

    def __init__(self, name, tummy_points=0):
        self.name = name
        self.tummy_points = tummy_points

    def is_tummy_rumbling(self):
        """Every creature must decide whether its tummy is making noises."""
        raise NotImplementedError(
            "This creature has forgotten how hunger works!"
        )

    def food_suck(self, snack_attack):
        """Each creature must know how to slurp up its food."""
        raise NotImplementedError(
            "This creature does not know how to eat. Very suspicious."
        )

    def __str__(self):
        # Politely ask the creature whether it wants snacks.
        if self.is_tummy_rumbling():
            return f"The {self.name} needs food"

        return f"The {self.name} doesn't need food"


class Fish(AquariumCreature):
    """A fishy little creature that absorbs 60% of its food."""

    FULL_TUMMY_NUMBER = 10
    FOOD_SUCK_POWER = 0.60

    def is_tummy_rumbling(self):
        # Below 10 tummy points means the fish demands room service.
        return self.tummy_points < self.FULL_TUMMY_NUMBER

    def food_suck(self, snack_attack):
        # Fish are messy eaters, so only 60% enters the fish dimension.
        actual_yum_yum = snack_attack * self.FOOD_SUCK_POWER
        self.tummy_points += actual_yum_yum


class Plant(AquariumCreature):
    """A suspiciously hungry plant that absorbs 50% of its food."""

    FULL_TUMMY_NUMBER = 15
    FOOD_SUCK_POWER = 0.50

    def is_tummy_rumbling(self):
        # Yes, aquarium plants have imaginary stomachs now.
        return self.tummy_points < self.FULL_TUMMY_NUMBER

    def food_suck(self, snack_attack):
        # Half becomes plant fuel. The other half vanishes into the wet void.
        actual_yum_yum = snack_attack * self.FOOD_SUCK_POWER
        self.tummy_points += actual_yum_yum


class Aquarium:
    """The glass kingdom where fish and plants demand snacks."""

    def __init__(self):
        self.wet_little_roommates = []

    def add_creature(self, new_water_friend):
        """Adds another hungry resident to the glass kingdom."""
        self.wet_little_roommates.append(new_water_friend)

    def feed(self, giant_food_blob):
        """Divides food equally among creatures that are still hungry."""

        hungry_gang = [
            water_friend
            for water_friend in self.wet_little_roommates
            if water_friend.is_tummy_rumbling()
        ]

        if not hungry_gang:
            print("Nobody wants food. The aquarium rejects your generosity.")
            return

        # Fairness has entered the aquarium.
        tiny_food_blob = giant_food_blob / len(hungry_gang)

        for hungry_goblin in hungry_gang:
            hungry_goblin.food_suck(tiny_food_blob)

    def show_aquarium_drama(self):
        """Reports the current hunger drama."""
        for water_friend in self.wet_little_roommates:
            print(water_friend)


def main():
    glass_fish_mansion = Aquarium()

    # The fish begin with 3 tummy points so the result matches
    # the assignment's example after the first feeding.
    goldfish_bob = Fish("goldfish", tummy_points=3)
    clownfish_bonald = Fish("clownfish", tummy_points=3)

    # The plants begin completely snackless. A tragic beginning.
    seaweed_steve = Plant("seaweed")
    kelp_kelvin = Plant("kelp")

    # Everybody gets thrown into the fancy glass puddle.
    glass_fish_mansion.add_creature(goldfish_bob)
    glass_fish_mansion.add_creature(clownfish_bonald)
    glass_fish_mansion.add_creature(seaweed_steve)
    glass_fish_mansion.add_creature(kelp_kelvin)

    print("Before feeding:")
    glass_fish_mansion.show_aquarium_drama()

    print("\nAfter feeding with 50:")
    print("Feeding with 50")

    # Release the first food blob!
    glass_fish_mansion.feed(50)
    glass_fish_mansion.show_aquarium_drama()

    print("\nAfter feeding with 80:")
    print("Feeding with 80")

    # A second, significantly chunkier food blob approaches.
    glass_fish_mansion.feed(80)
    glass_fish_mansion.show_aquarium_drama()

if __name__ == "__main__":
    # The aquarium drama officially begins.
    main()