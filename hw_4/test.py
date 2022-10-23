class A:
    s = [1, 2]

a = A()
b = A()

print(a.s, b.s)

b.s.append(3)
print(a.s, b.s)