import math

radius = float(input("Enter the radius of a circle: "))

area = math.pi * pow(radius,2)
print(f"the circumference is: {round(area,2)}cm^2")