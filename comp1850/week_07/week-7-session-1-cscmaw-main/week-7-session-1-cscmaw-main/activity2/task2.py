# Create an updated version of the Rectangle class from activity1/task2 with the following methods:
# (1) area method to return the area of a rectangle
# (2) perimeter method to return the perimeter of a rectangle






# Once completed, create 2 instances of Rectangles with:
# (1) first rectangle with width = 4 and height = 40
# (2) second rectangle with width = 3.5 and height=35.9
# After that, print the area and perimeter of both rectangle instances.




# Did you have setters with validation? Can the value of width and height be negative?
# If you have not, update the setters with validation for the width and height.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
rectangle1 = Rectangle(4, 40)
rectangle2 = Rectangle(3.5, 35.9)
print("Rectangle 1:")
print("Area:", rectangle1.area())
print("Perimeter:", rectangle1.perimeter())
print("Rectangle 2:")
print("Area:", rectangle2.area())  
print("Perimeter:", rectangle2.perimeter())