import numbers


class Pair:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def __add__(self, other):
        if isinstance(other, numbers.Number):
            return Pair(self._x + other, self._y + other)
        if isinstance(other, Pair):
            return Pair(self._x + other.get_x(),
                        self._y + other.get_y())
        return False

    def __str__(self):
        return str(self._x) + " " + str(self._y)


a = Pair(3, 4)
b = Pair(0, 7)

c = a + b
#c = a.__add__(b)

d = a + 1.5
print(c)
print(d)