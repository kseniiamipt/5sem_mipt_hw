class A:
    def __init__(self):
        self.a = 0
    def update(self, dict):
        self.__dict__.update(dict)


def f():
    return 1

D = dict()
D["b"] = f
print(D)
x = A()
x.update(D)
x.c = f
print(x.c)
a = f
print(a())
print(x.b())
print(x.__dict__)