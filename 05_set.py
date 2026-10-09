products = [
    {"Name": "White tea", "Price": 123.5, "Quantity": 50, "Location": "Store A"},
    {"Name": "Black tea", "Price": 133.5, "Quantity": 5, "Location": "Store B"},
    {"Name": "Green tea", "Price": 140.5, "Quantity": 15, "Location": "Store A"}
]

unique_locations = set()

for product in products:
    unique_locations.add(product["Location"])

print(unique_locations)