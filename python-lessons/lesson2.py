class Shape:
    def __init__(self, name):
        self.name = name

    def area (self):
        return 0

class Rectangle (Shape):
    def __init__ (self, name, width, height):
        super(). __init__(name)
        self.width = width
        self.height = height
    
    def area (self):
        super().area()
        return self.width * self.height
    
class Square (Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side
    
    def area (self):
        super().area()
        return self.side * self.side

if __name__ == "__main__":
    r = Rectangle("rectangle", 5, 10)
    rectangle = r.area()

    s = Square("square", 5)
    square = s.area()

    print (f"{r.area()}")
    print (f"{s.area()}")
