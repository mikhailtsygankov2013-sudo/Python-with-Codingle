
import math
 
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius * self.radius
    
    def perimeter(self):
        return 2 * math.pi * self.radius
 
radius = float(input("Enter the radius of circle: "))
circle = Circle(radius)
 
area_value = circle.area()
perimeter_value = circle.perimeter()
 
print("Radius: " + str(radius))
print("Area: " + str(round(area_value, 2)))
print("Perimeter: " + str(round(perimeter_value, 2)))
