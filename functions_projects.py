# =========================
# Functions - Projects
# =========================


# Task 1: Even or Odd
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"


# Task 2: Basic Operations
def basic_operations(operation, number1, number2):
    if operation == "add":
        return number1 + number2
    elif operation == "subtract":
        return number1 - number2
    elif operation == "multiply":
        return number1 * number2
    elif operation == "divide":
        if number2 == 0:
            raise ValueError("Cannot divide by zero")
        return number1 / number2
    else:
        raise ValueError("Invalid operation")


# Task 3: Total Points
def total_points(results):
    points = 0

    for result in results:
        team_score, opponent_score = result.split(":")
        team_score = int(team_score)
        opponent_score = int(opponent_score)

        if team_score > opponent_score:
            points += 3
        elif team_score == opponent_score:
            points += 1

    return points


# Task 4: The Largest Number
def largest_number(a, b, c):
    possible_results = [
        a + b + c,
        a * b * c,
        (a + b) * c,
        a * (b + c),
        a + b * c,
        a * b + c,
    ]

    return max(possible_results)


# Task 5: Power of N-th
def index(numbers, n):
    if n < 0 or n >= len(numbers):
        return -1

    return numbers[n] ** n


# Task 6: Quarter of the Year
def quarter_of_the_year(month):
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")

    return (month - 1) // 3 + 1


# Task 7: Century from Year
def century(year):
    if year <= 0:
        raise ValueError("Year must be a positive integer")

    return (year + 99) // 100


# Task 8: Form the Minimum
def form_the_minimum(digits):
    unique_digits = sorted(set(digits))
    number_as_text = "".join(str(digit) for digit in unique_digits)

    return int(number_as_text)


# =========================
# The Pizza Madness
# =========================


# Task 1: String Repeat
def string_repeat(number, text):
    return text * number


# Task 2: No Whitespaces
def no_space(text):
    return text.replace(" ", "")


# Task 3: Number to String
def number_to_string(number):
    return str(number)


# Task 4: Boolean to String
def boolean_to_string(value):
    return str(value)


# Task 5: Abbreviate a Pizza Name
def abbrev_name(name):
    words = name.split()
    return f"{words[0][0].upper()}.{words[1][0].upper()}"


# Task 6: Pizza Length
def name_length(name):
    words = name.split()
    return [f"{word} {len(word)}" for word in words]


# Task 7: Remove the First and Last Element
def remove_orders(orders):
    items = orders.split(",")

    if len(items) <= 2:
        return ""

    return ",".join(items[1:-1])


# Task 8: The Menu
def food_menu(food_items):
    return [
        f"{position}. {food}"
        for position, food in enumerate(food_items, start=1)
    ]


# =========================
# Optional tests
# =========================

if __name__ == "__main__":
    print("Functions - Projects")
    print(even_or_odd(8))                          # Even
    print(basic_operations("multiply", 4, 5))     # 20
    print(total_points(["3:1", "1:1", "0:2"]))    # 4
    print(largest_number(1, 2, 3))                # 9
    print(index([1, 2, 3, 4], 2))                 # 9
    print(quarter_of_the_year(8))                 # 3
    print(century(1905))                          # 20
    print(form_the_minimum([1, 3, 6, 2, 3]))      # 1236

    print("\nThe Pizza Madness")
    print(string_repeat(2, "HawaiiPizza"))
    print(no_space("Hawaii Pizza"))
    print(number_to_string(123))
    print(boolean_to_string(True))
    print(abbrev_name("Hawaii Pizza"))
    print(name_length("hawaii pizza"))
    print(remove_orders("1,2,3,4"))
    print(food_menu(["Hawaii Pizza", "Diablo Pizza"]))