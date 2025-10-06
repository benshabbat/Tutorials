# Package Creation
#  Create a package called shapes with two modules: circle.py and rectangle.py.
#  Each should contain functions to calculate area and perimeter.
#  Import and use them.

import circle
import rectangle

radius = 5
length = 10
width = 4

print("Circle:")
print(f"Area: {circle.calculate_area(radius)}")
print(f"Perimeter: {circle.calculate_perimeter(radius)}")

print("\nRectangle:")
print(f"Area: {rectangle.calculate_area(length, width)}")
print(f"Perimeter: {rectangle.calculate_perimeter(length, width)}")


# Using __name__ == "__main__"
#  Write a module that has both functions
# and a test section that only runs when executed directly.

# def greet(name):
#     return f"Hello, {name}!"

# def farewell(name):
#     return f"Goodbye, {name}!"

  
# if __name__ == "__main__":
#     print(greet("Alice"))
#     print(greet("Bob"))
#     print(greet("Charlie"))
#     print(farewell("Alice"))
#     print(farewell("Bob"))
#     print(farewell("Charlie"))


    