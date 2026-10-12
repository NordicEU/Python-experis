class BaseProduct:
    def __init__(self, name, price, description = ""):
        self.name = name
        self.price = price
        self.description = description

    def apply_discount(self, discount_percentage):
            discount_amount = self.price * (discount_percentage / 100)
            self.price -= discount_amount

    def __str__(self):
        return f"BaseProduct(name={self.name}, price={self.price}, description={self.description})"
        