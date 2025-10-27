# Define a Circle class with a single field named radius. The value for radius is passed
# when an instance of Circle is created. In this class, define the following methods:
# (1) get_radius to return the radius of the circle
# (2) perimeter to return the perimeter of the circle, perimeter = 2 * Pi * radius (you can set Pi = 3.142)
# (3) area to return the area of a circle, area = Pi * radius * radius








# Once completed, create two instances of Circle with different radius, eg 4.5, 10.8
# and print the radius, perimeter, and area for both instances




# Did you create a setter for radius? Can the radius be a negative number?
# If you have not, create a setter for radius with validation.
class Circle:
    def __init__(self, radius,Pi=3.142):
        self.radius = radius
        self.Pi = Pi
    def get_radius(self):
        return self.radius
    def perimeter(self):
        return 2 * self.Pi * self.radius
    def area(self):
        return self.Pi * self.radius * self.radius
circle1 = Circle(4.5)
circle2 = Circle(10.8)
print("Circle 1:")
print("Radius:", circle1.get_radius())
print("Perimeter:", circle1.perimeter())
print("Area:", circle1.area())