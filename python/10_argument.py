def average(*args):
    return sum(args) / len(args)

print(average(1, 2, 5, 8, 10))  # Output: 5.2


def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet(name="Messi", age=39, city="Barcelona")  # Output: name: Messi
                               #         age: 39
                               #         city: Barcelona
greet(name="Ronaldo", age=38, country="Portugal")  # Output: name: Ronaldo
                                                   #         age: 38
                                                   #         country: Portugal
print("d","e","w","q", sep="---")