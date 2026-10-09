product = {
    "Name": "White tea",
    "Price": 123.5,
    "Quantity": 50
}

# print(product["Name"])

product["Description"] = """
Multi
A tea made from the leaves of the Camellia sinensis plant.
Line
"""
# print(product["Description"])

# prnt(product["Weight"]) KeyError: 'Weight'

# for key in product:
#     print(key, product[key])

for key, value in product.items():
    print(f"{key} -> {value}")


