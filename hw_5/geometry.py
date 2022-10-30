class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def __str__(self):
        return "[" + str(self._x) + ", " + str(self._y) + "]"


def dist(a, b):
    return ((b.get_y() - a.get_y()) ** 2 + (b.get_x() - a.get_x()) ** 2) ** 0.5


class Shape:
    def __init__(self, type="Shape"):
        self._type = type

    def __str__(self):
        return str(self._type)


class Polygon(Shape):
    def __init__(self, type = "Polygon"):
        super().__init__(type)
        self._points = []

    def perimeter(self):
        p = 0
        for i in range(len(self._points) - 1):
            p += dist(self._points[i], self._points[i+1])
        return p + dist(self._points[-1], self._points[0])

    # реализация площади через разбивку на треугольники
    def area(self):
        s = 0
        for i in range(len(self._points)-1):
            s += self._points[i]._x * self._points[i+1]._y - self._points[i]._y * self._points[i+1]._x
        s += self._points[len(self._points)-1]._x * self._points[0]._y - self._points[len(self._points)-1]._y * self._points[0]._x
        s = abs(s/2)
        return s

    def __str__(self):
         return '{}, perimeter={}, area={}'.format(super().__str__(), self.perimeter(), self.area())

class Triangle(Polygon):
    def __init__(self, p1, p2, p3, type="Triangle"):
        super().__init__(type)
        self._points.append(p1)
        self._points.append(p2)
        self._points.append(p3)

    def __str__(self):
         return '{}, points: {},{},{}'.format(super().__str__(), self._points[0].__str__(), self._points[1].__str__(),
                                              self._points[2].__str__())


class Parallelogram(Polygon):
    def __init__(self, p1, p2, p3, p4, type="Parallelogram"):
        super().__init__(type)
        self._points.append(p1)
        self._points.append(p2)
        self._points.append(p3)
        self._points.append(p4)

    def __str__(self):
         return '{}, points: {},{},{}'.format(super().__str__(), self._points[0].__str__(), self._points[1].__str__(),
                                              self._points[2].__str__(), self._points[3].__str__())


class Rhombus(Parallelogram):
    def __init__(self, p1, p2, p3, p4, type="Rhombus"):
        super().__init__(type)


class Rectangle(Parallelogram):
    def __init__(self, p1, p2, p3, p4, type="Rectangle"):
        super().__init__(type)


class Square(Rectangle, Rhombus):
    def __init__(self, p1, p2, p3, p4, type="Square"):
        super().__init__(type)


class Circle(Shape):
    def __init__(self, radius, centre, type = "Circle"):
        super().__init__(type)
        self._radius = radius
        self._centre = centre

    def __str__(self):
        return '{}, perimeter={}, area={}, radius={}, centre={}'.format(super().__str__(),
                                                                        self.perimeter(), self.area(),
                                                                        self._radius, self._centre.__str__())

    def area(self):
        import math
        return math.pi * self._radius**2

    def perimeter(self):
        import math
        return 2 * math.pi * self._radius



a = Triangle(Point(0,0), Point(2,0), Point(0, 3))
print(a)
print()

b = Circle(6, Point(7,7))
print(b)
print()
