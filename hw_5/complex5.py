import numpy as np
import numbers


class Exception_Complex_to_exp(Exception):
    pass


class Complex:
    def __init__(self, a=None, b=None, r=None, f=None):
        self.set_a(a)
        self.set_b(b)
        self.set_r(r)
        self.set_f(f)

    def get_a(self):
        return self._a

    def get_b(self):
        return self._b

    def get_r(self):
        return self._r

    def get_f(self):
        return self._f

    def set_a(self, a):
        if isinstance(a, numbers.Number) or a==None:
            self._a = a
        else:
            raise ValueError

    def set_b(self, b):
        if isinstance(b, numbers.Number) or b==None:
            self._b = b
        else:
            raise ValueError

    def set_r(self, r):
        if isinstance(r, numbers.Number) or r==None:
            self._r = r
        else:
            raise ValueError

    def set_f(self, f):
        if isinstance(f, numbers.Number) or f==None:
            self._f = f
        else:
            raise ValueError

    def complex_to_exp(self):
        self._r = (self._a**2 + self._b**2)**0.5

        if self._a > 0 and self._b > 0:
            self._f = np.arctan(self._b/self._a)

        if self._a < 0 and self._b > 0:
            self._f = np.pi - np.arctan(self._b/abs(self._a))

        if self._a < 0 and self._b < 0:
            self._f = np.pi + np.arctan(abs(self._b)/abs(self._a))

        if self._a > 0 and self._b < 0:
            self._f = 2 * np.pi - np.arctan(abs(self._b)/self._a)

        if self._a == 0 and self._b > 0:
            self._f = np.pi/2

        if self._a == 0 and self._b < 0:
            self._f = - np.pi / 2

        if self._a == 0 and self._b == 0:
            raise Exception_Complex_to_exp()

        if self._a > 0 and self._b == 0:
            self._f = 0

        if self._a < 0 and self._b == 0:
            self._f = np.pi

    def exp_to_complex(self):
        if self._r == 0:
            self._a, self._b = 0, 0
        else:
            self._a = np.cos(self._f) * self._r
            self._b = np.sin(self._f) * self._r

    def __add__(self, other):
        if self._a == None:
            self.exp_to_complex()
        if other._a == None:
            other.exp_to_complex()
        new = Complex(a=self._a+other._a, b=self._b+other._b)
        new.complex_to_exp()

        return Complex(a=self._a+other._a, b=self._b+other._b, r=new.get_r(), f=new.get_f())

    def __sub__(self, other):
        if self._a == None:
            self.exp_to_complex()
        if other._a == None:
            other.exp_to_complex()
        new = Complex(a=self._a - other._a, b=self._b - other._b)
        new.complex_to_exp()

        return Complex(a=self._a-other._a, b=self._b-other._b, r=new.get_r(), f=new.get_f())

    def __mul__(self, other):
        if self._r == None:
            self.complex_to_exp()
        if other._r == None:
            other.complex_to_exp()
        new = Complex(r=self._r*other._r, f=self._f + other._f)
        new.exp_to_complex()

        return Complex(a=new.get_a(), b=new.get_b(),
                       r=self._r*other._r, f=self._f + other._f)

    def __truediv__(self, other):
        if self._r == None:
            self.complex_to_exp()
        if other._r == None:
            other.complex_to_exp()
        new = Complex(r=self._r / other._r, f=self._f - other._f)
        new.exp_to_complex()
        return Complex(a=new.get_a(), b=new.get_b(),
                       r=self._r / other._r, f=self._f - other._f)

    def __abs__(self):
        if self._a is None:
            self.exp_to_complex()
        return round(np.sqrt((self._a ** 2) + (self._b**2)), 2)

    def __eq__(self, other):
        if self._a is None:
            self.exp_to_complex()
        if other.get_a() is None:
            other.exp_to_complex()
        if self._r is None:
            self.complex_to_exp()
        if other.get_r() is None:
            other.complex_to_exp()
        if self._a == other.get_a() and self._b == other.get_b():
            return True
        else:
            return False

    def __str__(self):
        return "a:" + f"%.{3}f" % self._a + \
               " b:" + f"%.{3}f" % self._b + \
               " | r:" + f"%.{3}f" % self._r + \
               " f:" + f"%.{3}f" % self._f

    def __getitem__(self, key):
        if key != 0 and key != 1:
            return False
        if self._a is None:
            self.exp_to_complex()
        if key == 0:
            return self._a
        return self._b

    def __setitem__(self, key, value):
        if key != 0 and key != 1:
            return False
        if self._a is None:
            self.exp_to_complex()
        if key == 0:
            self._a = value
        else:
            self._b = value

'''print("\nTEST error value")
q = Complex(a='svd', b=30)
w = Complex(a=3, b=0)
c = q+w
print(c)'''

print("\nTEST error exp")
q = Complex(a=0, b=0)
w = Complex(a=3, b=0)
c = q+w
q.complex_to_exp()
print(c)
