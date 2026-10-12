from Product import Product

class Product:
    name = ""
    price = 0
    quantity = 0
    location = ""
    weight = 0  # New attribute added to the Product class

    def __init__(self, name, price, quantity, location, weight):
            self.name = name
            self.price = price
            self.quantity = quantity
            self.location = location
            self.weight = weight

    def is_in_stock(self):
        return self.quantity > 0
    def apply_discount(self, discount_percentage):
        discount_amount = self.price * (discount_percentage / 100)
        self.price -= discount_amount

    def restock(self, additional_quantity):
        self.quantity += additional_quantity


white_tea = Product("White tea", 120, 40, "Store A", 10)
# white_tea = Product()
# white_tea.name = "White tea"
# white_tea.price = 120
# white_tea.quantity = 40
# white_tea.location = "Store A"
# white_tea.weight = 10  # Adding a new attribute to the Product class

print(white_tea.is_in_stock())  # Should print True
white_tea.price = 100

white_tea.apply_discount(10)

print(white_tea.price)  # Should print 90
white_tea.restock(10)

print(white_tea.quantity)  # Should print 50