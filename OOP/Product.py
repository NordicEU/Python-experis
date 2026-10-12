from BaseProduct import BaseProduct
class Product(BaseProduct):

    def __init__(self, name, price, quantity, location, weight):
            super().__init__(name, price)
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

    def get_total_value(self):
        return self.price * self.quantity

    @staticmethod
    def is_valid_product_name(name):
        return isinstance(name, str) and len(name) > 0

    def __str__(self):
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity}, location={self.location}, weight={self.weight})"
    