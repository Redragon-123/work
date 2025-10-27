class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"
point1 = Point(3, 4)
print(str(point1))   
print(repr(point1))  

# Given a Point class, define the __str__ and __repr__ methods
