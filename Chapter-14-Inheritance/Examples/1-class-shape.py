"""
define a class shape
inherit two classes Circle and Rectangle.
Check the inheritance relationship between the classes
"""

class Shape:
    pass

class Rectangle(Shape):
    pass

class Circle(Shape):
    pass

s = Shape()
c = Circle()

print(isinstance(s, Shape))
print(isinstance(s, Rectangle))
print(isinstance(s, Circle))

print(issubclass(Rectangle, Shape))
print(issubclass(Circle, Shape))