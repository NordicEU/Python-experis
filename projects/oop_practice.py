class AquariumCreature:
    """The parent class for anything chilling in the aquarium."""

    def __init__(self, name, tummy_points=0):
        self.name = name
        self.tummy_points = tummy_points

    def is_tummy_rumbling(self):
        """Checks whether this aquatic citizen demands snacks."""
        raise NotImplementedError(
            "This creature has forgotten how hunger works!"
        )

    def food_suck(self, snack_attack):
        """Lets the creature absorb some incoming food."""
        raise NotImplementedError(
            "This creature does not know how to eat. Very suspicious."
        )

    def digest_food(self):
        """Removes food during one sleep cycle."""
        raise NotImplementedError(
            "This creature has forgotten how digestion works!"
        )

    def __str__(self):
        if self.is_tummy_rumbling():
            hunger_message = "needs food"
        else:
            hunger_message = "doesn't need food"

        return (
            f"The {self.name} {hunger_message} "
            f"(food level: {self.tummy_points:.2f})"
        )


class Fish(AquariumCreature):
    """A fishy little creature that absorbs 60% of its food."""

    FULL_TUMMY_NUMBER = 10
    FOOD_SUCK_POWER = 0.60
    FOOD_USED_PER_SLEEP = 3

    def is_tummy_rumbling(self):
        # Below 10 tummy points means the fish demands room service.
        return self.tummy_points < self.FULL_TUMMY_NUMBER

    def food_suck(self, snack_attack):
        # Only 60% enters the mysterious fish dimension.
        actual_yum_yum = snack_attack * self.FOOD_SUCK_POWER
        self.tummy_points += actual_yum_yum

    def digest_food(self):
        # Even sleeping fish need energy for important fish business.
        self.tummy_points -= self.FOOD_USED_PER_SLEEP

        # Negative food does not exist, despite what the fish accountants say.
        if self.tummy_points < 0:
            self.tummy_points = 0


class Plant(AquariumCreature):
    """A suspiciously hungry plant that absorbs 50% of its food."""

    FULL_TUMMY_NUMBER = 15
    FOOD_SUCK_POWER = 0.50
    FOOD_USED_PER_SLEEP = 4

    def is_tummy_rumbling(self):
        # Yes, aquarium plants have imaginary stomachs now.
        return self.tummy_points < self.FULL_TUMMY_NUMBER

    def food_suck(self, snack_attack):
        # Half becomes plant fuel. The rest vanishes into the wet void.
        actual_yum_yum = snack_attack * self.FOOD_SUCK_POWER
        self.tummy_points += actual_yum_yum

    def digest_food(self):
        # Growing dramatically overnight is apparently exhausting.
        self.tummy_points -= self.FOOD_USED_PER_SLEEP

        # Plants are not allowed to owe food to the aquarium bank.
        if self.tummy_points < 0:
            self.tummy_points = 0


class Aquarium:
    """The glass kingdom where fish and plants demand snacks."""

    def __init__(self):
        self.wet_little_roommates = []
        self.day_number = 1

    def add_creature(self, new_water_friend):
        """Adds a creature to the aquarium."""
        self.wet_little_roommates.append(new_water_friend)

    def get_hungry_gang(self):
        """Returns all creatures currently demanding snacks."""
        return [
            water_friend
            for water_friend in self.wet_little_roommates
            if water_friend.is_tummy_rumbling()
        ]

    def feed(self, giant_food_blob):
        """Divides food equally among creatures that currently need it."""

        hungry_gang = self.get_hungry_gang()

        if not hungry_gang:
            print("\nNobody needs food.")
            print("The aquarium rejects your unnecessary generosity!")
            return

        # Aquarium democracy: every hungry citizen gets an equal portion.
        tiny_food_blob = giant_food_blob / len(hungry_gang)

        print(
            f"\n{len(hungry_gang)} hungry creatures will receive "
            f"{tiny_food_blob:.2f} units each."
        )

        for hungry_goblin in hungry_gang:
            tummy_before = hungry_goblin.tummy_points

            hungry_goblin.food_suck(tiny_food_blob)

            tummy_after = hungry_goblin.tummy_points
            food_actually_sucked = tummy_after - tummy_before

            print(
                f"The {hungry_goblin.name} sucked up "
                f"{food_actually_sucked:.2f} units!"
            )

    def sleep(self):
        """Advances the simulation by one sleep cycle."""

        print("\nThe aquarium lights have been turned off.")
        print("Everyone is sleeping and using up food...")

        for sleepy_water_friend in self.wet_little_roommates:
            tummy_before = sleepy_water_friend.tummy_points

            sleepy_water_friend.digest_food()

            food_used = (
                tummy_before - sleepy_water_friend.tummy_points
            )

            print(
                f"The {sleepy_water_friend.name} used "
                f"{food_used:.2f} tummy points while sleeping."
            )

        self.day_number += 1

        print("\nThe aquarium lights turn back on.")
        print(f"Day {self.day_number} has begun!")

    def show_aquarium_drama(self):
        """Reports the latest aquarium hunger drama."""

        print(f"\n--- Aquarium status: Day {self.day_number} ---")

        for water_friend in self.wet_little_roommates:
            print(water_friend)

        print("--------------------------------")


def ask_for_food_amount():
    """Keeps asking until the user enters a valid food amount."""

    while True:
        food_answer = input(
            "How many units of food would you like to add? "
        ).strip()

        try:
            giant_food_blob = float(food_answer)

            if giant_food_blob <= 0:
                print("The food amount must be greater than zero.")
                print("You cannot feed the fish imaginary negative snacks.")
                continue

            return giant_food_blob

        except ValueError:
            print("Please enter a number, such as 50 or 12.5.")
            print("The fish are not currently accepting words as payment.")


def ask_what_to_do():
    """Asks the player to feed, sleep, or quit."""

    while True:
        print("\nWhat would you like to do?")
        print("1. Feed the creatures")
        print("2. Sleep for one cycle")
        print("3. Quit the aquarium")

        player_choice = input("Choose 1, 2, or 3: ").strip().lower()

        # Accept both numbers and words to make the fish more cooperative.
        if player_choice in ("1", "feed", "f", "yes", "y"):
            return "feed"

        if player_choice in ("2", "sleep", "s", "no", "n"):
            return "sleep"

        if player_choice in ("3", "quit", "q", "exit"):
            return "quit"

        print("\nThat is not a valid choice.")
        print("The goldfish tried to understand it but forgot halfway through.")


def main():
    glass_fish_mansion = Aquarium()

    # The fish begin with three tummy points so the original task's
    # first feeding example still works correctly.
    goldfish_bob = Fish("goldfish", tummy_points=3)
    clownfish_bonald = Fish("clownfish", tummy_points=3)

    # The plants begin snackless. Their tragic origin story continues.
    seaweed_steve = Plant("seaweed")
    kelp_kelvin = Plant("kelp")

    # Everybody moves into the suspiciously expensive glass puddle.
    glass_fish_mansion.add_creature(goldfish_bob)
    glass_fish_mansion.add_creature(clownfish_bonald)
    glass_fish_mansion.add_creature(seaweed_steve)
    glass_fish_mansion.add_creature(kelp_kelvin)

    print("Welcome to the Aquarium of Questionable Decisions!")

    aquarium_is_open = True

    while aquarium_is_open:
        # Show the latest chaos at the start of every cycle.
        glass_fish_mansion.show_aquarium_drama()

        player_choice = ask_what_to_do()

        if player_choice == "feed":
            if not glass_fish_mansion.get_hungry_gang():
                print("\nEveryone is currently full!")
                print("The creatures stare at the extra food judgmentally.")
            else:
                giant_food_blob = ask_for_food_amount()

                print(
                    f"\nReleasing {giant_food_blob:.2f} units of food!"
                )

                glass_fish_mansion.feed(giant_food_blob)

                print("\nThe feeding frenzy is complete!")

        elif player_choice == "sleep":
            glass_fish_mansion.sleep()

        elif player_choice == "quit":
            print("\nGoodnight!")
            print("The aquarium creatures will now stare into the void.")
            aquarium_is_open = False


if __name__ == "__main__":
    # The looping aquarium drama officially begins.
    main()