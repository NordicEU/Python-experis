def fizzbuzz(n):

    if not isinstance(n, int):
        raise ValueError("Input must be an integer")

    if n <= 0:
        raise ValueError("Input must be positive")

    result = []

    for number in range(1, n + 1):

        if number % 15 == 0:
            result.append("FizzBuzz")
        elif number % 3 == 0:
            result.append("Fizz")
        elif number % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(number))

    return result