product1Name = "green tea"
product2Name = "black tea"
product3Name = "white tea"

# print(product1Name)
# print(product2Name)
# print(product3Name)

productNames = ["green tea", "black tea", "white tea"]

# Shortcut to comment out multiple lines in VS Code: Ctrl + K + C

# print(productNames[0])
# print(productNames[1])
# print(productNames[2])

# for productName in productNames:
#     print(productName)

# print(productNames[3]) IndexError: list index out of range

# for i in range(3):
#     print(f"{i}. {productNames[i]}")

mixedList = ["name", 25]

# for item in mixedList:
#     print(item)

productNames.append("Brown tea")
productNames.insert(2, "Yellow tea")

productNames[0] = "Purple tea"

# for productName in productNames:
#     print(productName)

# print(len(productNames))
# print(min(productNames))
# print(max(productNames))

print(productNames[1:4:2])

print(productNames[::-1])