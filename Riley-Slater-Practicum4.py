

import matplotlib.pyplot as plt

currencies = ["Euro", "Pound", "Swiss Franc", "Sri Lankan Rupee"]

conversions = [1.11, 1.31, 1.01, .0055]

color = ["green"]
for loop in range(len(currencies)-1):
    if color[loop] == "green":
        color.append("red")
    else:
        color.append("green")

plt.scatter(x=currencies, y=conversions, c=color, marker="*")

plt.xlabel("Currency")
plt.ylabel("Conversion To $")
plt.title("Currency Conversion Visualization")

plt.show()



"""
import numpy as np

size = int(input("Enter a  positive integer: "))
numbers = np.random.randint(0, 11, size*size)
numbers.resize(size, size)
print(numbers)

def minor_diagonal(numbers):
    total = 0
    slicer = len(numbers)
    for loop in numbers:
        slicer -= 1
        total += (loop[slicer])
    return total
print("Minor diagonal sum =", minor_diagonal(numbers))
"""

"""
class Rectangle():
    def __init__(self, name, base, height):
        self.name = name
        self.height = height
        self.base = base

    def __str__(self):
        return self.name +" has area "+ str(self.base * self.height)

class Square(Rectangle):
    def __init__(self, name, base):
        self.name = name
        self.side = base

    def __str__(self):
        return self.name + " has area " + str(self.side**2)



r1 = Rectangle("Rectangle 1", 5, 6)
print(r1)
s1 = Square("Square 1", 7)
print(s1)
"""

"""
def calculate(file_name):
    result = 0
    with open(file_name, 'r') as file:
        for loop in file:
            data = loop.split('-')
            amount = data[0]
            exchange = data[2]
            result += round(float(amount) * float(exchange), 2)
    print("Value = $"+ str(result))

            
calculate("currency.txt")
"""
