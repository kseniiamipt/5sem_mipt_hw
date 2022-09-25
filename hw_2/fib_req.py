def fib_r(n):
    if n == 0:
        return 0
    if (n) in (1, 2):
        return 1
    return fib_r(n - 1) + fib_r(n - 2)
# print(fib_r(9))