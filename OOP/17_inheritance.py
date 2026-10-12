from Product import Product
from VirtualProduct import VirtualProduct

white_tea = Product("White tea", 100, 20, "Store A", 10)

e_book = VirtualProduct("The Hail Mary Project", 50, "https://example.com/download")

products = {white_tea, e_book}

for product in products:
    print(product)
