class Creature:
    def __init__(self, name, food=0):
        self.name, self.food = name, food

    def hungry(self):
        return self.food < self.limit

    def eat(self, amount):
        self.food += amount * self.rate

    def sleep(self):
        before = self.food
        self.food = max(0, self.food - self.loss)
        return before - self.food

    def __str__(self):
        status = "needs food" if self.hungry() else "doesn't need food"
        return f"The {self.name} {status} (food level: {self.food:.2f})"


class Fish(Creature):
    limit, rate, loss = 10, .6, 3


class Plant(Creature):
    limit, rate, loss = 15, .5, 4


class Aquarium:
    def __init__(self):
        self.creatures = [
            Fish("goldfish", 3),
            Fish("clownfish", 3),
            Plant("seaweed"),
            Plant("kelp")
        ]
        self.day = 1

    def hungry(self):
        return [x for x in self.creatures if x.hungry()]

    def show(self):
        print(f"\n--- Aquarium status: Day {self.day} ---")
        print(*self.creatures, sep="\n")

    def feed(self, food):
        hungry = self.hungry()
        if not hungry:
            print("\nEveryone is full!")
            return
        share = food / len(hungry)
        for creature in hungry:
            before = creature.food
            creature.eat(share)
            print(f"{creature.name} absorbed {creature.food - before:.2f} units.")

    def sleep(self):
        print("\nEveryone goes to sleep...")
        for creature in self.creatures:
            print(f"{creature.name} used {creature.sleep():.2f} food.")
        self.day += 1


def get_food():
    while True:
        try:
            food = float(input("Food amount: "))
            if food > 0:
                return food
        except ValueError:
            pass
        print("Enter a number greater than zero.")


def main():
    aquarium = Aquarium()
    while True:
        aquarium.show()
        choice = input("\n1. Feed\n2. Sleep\n3. Quit\nChoice: ").lower().strip()

        if choice in ("1", "feed", "f", "yes", "y"):
            aquarium.feed(get_food())
        elif choice in ("2", "sleep", "s", "no", "n"):
            aquarium.sleep()
        elif choice in ("3", "quit", "q", "exit"):
            print("\nGoodnight!")
            break
        else:
            print("\nInvalid choice.")


if __name__ == "__main__":
    main()
