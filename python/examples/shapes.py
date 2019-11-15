class Point:
    """
    Represents a 2D math point.
    """
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        print("Calling")
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, value):
        self.__x = value

    @y.setter
    def y(self, value):
        self.__y = value

    def __repr__(self):
        return "Cosa({x},{y})".format(x=self.__x, y=self.__y)

    def __add__(self, point):
        return Point(self.__x + point.x, self.__y + point.y)

class Shape:
    def area():
        raise Exception("Area method not declared")

    def perimeter():
        raise Exception("Perimeter method not declared")

class Rectangle(Shape):
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def area(self):
        return self._length * self._width

    def perimeter(self):
        return self._length * 2 + self._width * 2

    def __repr__(self):
        return "Rectangle({length}, {width})".format(length=self._length, width=self._width)

class Circle(Shape):
    pi = 3.14

    def __init__(self, radius):
        self._radius = radius

    def area(self):
        return Circle.pi * (self._radius ^ 2)

    def perimeter(self):
        return 2 * Circle.pi * self._radius

    def __repr__(self):
        return "Circle({radius})".format(radius=self._radius)
