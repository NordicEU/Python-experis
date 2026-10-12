products = [
    {"Name": "White tea", "Price": 123.5, "Quantity": 50, "Location": "Store A"},
    {"Name": "Black tea", "Price": 133.5, "Quantity": 5, "Location": "Store B"},
    {"Name": "Green tea", "Price": 140.5, "Quantity": 15, "Location": "Store A"}
]

def is_in_stock(product):
    return product["Quantity"] > 0

def apply_discount(product, discount_percentage):
    discount_amount = product["Price"] * (discount_percentage / 100)
    product["Price"] -= discount_amount

def restock(product, additional_quantity):
    product["Quantity"] += additional_quantity

for product in products:
    print(is_in_stock(product))

apply_discount(products[1], 10)
print(products[1]["Price"])  # Should print the discounted price of Black tea

restock(products[2], 25)
print(products[2]["Quantity"])  # Should print the new quantity of Green tea