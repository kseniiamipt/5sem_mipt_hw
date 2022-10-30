def fib(n):
    if n == 1:
        print('0')
        return

    f1, f2 = 0, 1
    for i in range(n):
        yield f1
        f1, f2 = f2, f2+f1

for f in fib(6):
     print(f)
