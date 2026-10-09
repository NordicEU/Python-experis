def calculate_total(order_amount, shipping_fee):
    discount = 0.15 if order_amount > 200 else 0.05
    total = (order_amount - (order_amount * discount)) + shipping_fee
    return total, discount

my_total, my_discount = calculate_total(2000, 100)

print(f"Order Amount: ${2000}")
print(f"Discount applied: {my_discount * 100}%")

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

red[0] = 150 # Tuples are immutable, so this will raise an error. You cannot change the value of an element in a tuple after it has been created.

print(red[0])
