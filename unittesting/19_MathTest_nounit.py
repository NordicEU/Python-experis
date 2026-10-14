from Math import *

result = add(1,2)
if result != 3:
    raise AssertionError(f"Expected 3, but got {result}")

result = subtract(5,3)
if result != 2:
    raise AssertionError(f"Expected 2, but got {result}")   

result = multiply(4,5)
if result != 20:
    raise AssertionError(f"Expected 20, but got {result}")

result = divide(10,2)
if result != 5:
    raise AssertionError(f"Expected 5, but got {result}")   