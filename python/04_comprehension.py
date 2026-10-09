numbers = [1, 2, 3, 4, 5]

# duplicated_numbers = []

# for n in numbers:
#     duplicated_numbers.append(n * 2)
duplicated_numbers = [2 * n for n in numbers if n % 2 == 0]

print(duplicated_numbers)