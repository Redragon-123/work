import math

# Define a class Coordinate with fields x and y. The value to these fields
# are passed to the __init__ method when an instance of Coordinate is created.
# Define a setter method for x and for y, which only accept numbers.
# Then, define a method called distance. The distance method should take
# another instance of Coordinate as an argument and returns the distance between 
# the two coordinates. The formula to find the distance between the two coordinates,
# distance = √((x2 – x1)² + (y2 – y1)²). You can use math.sqrt() function for the square root
class Coordinate:
    def __init__(self, x, y):
        self.set_x(x)
        self.set_y(y)

    def set_x(self, x):
        if isinstance(x, (int, float)):
            self.x = x
        else:
            raise ValueError("x must be a number")

    def set_y(self, y):
        if isinstance(y, (int, float)):
            self.y = y
        else:
            raise ValueError("y must be a number")

    def distance(self, other):
        if not isinstance(other, Coordinate):
            raise ValueError("Argument must be an instance of Coordinate")
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)
coordinate1 = Coordinate(3, 4)
coordinate2 = Coordinate(9, 12)
print("Distance from coordinate1 to coordinate2:", coordinate1.distance(coordinate2))












# Once completed, create two instances of Coordinates:
# coordinate1 with x = 3, y = 4
# coordinate2 with x = 9, y = 12
# and print the distance between coordinate1 and coordinate2
# with the distance method in both coordinates. Are they the same?








# Once you have completed with the distance method, update the class definition with
# another method called slope to calculate the slope between the two coordinates.
# The formula for slop is (y2 - y1) /( x2 - x1). Then, print the slopes between the two coordinates
# you have created previously.
