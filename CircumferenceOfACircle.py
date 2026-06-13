import math
 
def calculate_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference
 
radius = float(input("Enter the radius of the circle: "))
result = calculate_circumference(radius)
 
print("Radius: " + str(radius))
print("Circumference: " + str(round(result, 2)))
