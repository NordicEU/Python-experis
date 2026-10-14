import random


class CowsAndBulls:

    def __init__(self):
        self.target = "".join(
            str(random.randint(0, 9))
            for _ in range(4)
        )

        self.guess_count = 0
        self.finished = False

    def guess(self, number):

        if self.finished:
            raise ValueError("Game already finished")

        if len(number) != 4 or not number.isdigit():
            raise ValueError("Guess must be 4 digits")

        self.guess_count += 1

        cows = 0
        bulls = 0

        target_remaining = []
        guess_remaining = []

        # Count cows first
        for i in range(4):
            if number[i] == self.target[i]:
                cows += 1
            else:
                target_remaining.append(self.target[i])
                guess_remaining.append# Count bulls from remaining digits
        for digit in guess_remaining:
            if digit in target_remaining:
                bulls += 1
                target_remaining.remove(digit)

        if cows == 4:
            self.finished = True

        return f"{cows} cow(s), {bulls} bull(s)"


def main():

    game = CowsAndBulls()

    print("Welcome to Cows and Bulls!")
    print("I have chosen a secret 4-digit number.")
    print("Try to guess it!")

    # Uncomment while testing
    print(f"DEBUG: {game.target}")

    while not game.finished:

        guess = input("\nEnter a 4-digit guess: ")

        try:
            result = game.guess(guess)

            print(result)
            print(f"Guesses made: {game.guess_count}")

            if game.finished:
                print("\n🎉 Congratulations!")
                print(f"You guessed the number {game.target}!")
                print(f"It took you {game.guess_count} guesses.")

        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()