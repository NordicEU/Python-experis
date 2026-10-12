from Product import Product
from VirtualProduct import VirtualProduct
from Order import Order

white_tea = Product("White tea", 100, 20, "Store A", 10)

e_book = VirtualProduct("The Hail Mary Project", 50, "https://example.com/download")

order = Order()
order.add_product(white_tea)
order.add_product(e_book)
order.display_details()
