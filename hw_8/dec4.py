import time
from functools import lru_cache


def time_decorator(func):
    def wrapper(*args, **kwargs):

        start_time = time.time()
        res = func(*args, **kwargs)
        res_time=time.time() - start_time
        return res, res_time
    return wrapper


@time_decorator
def fib_rec(n):
    if n == 0 or n == 1:
        return 1
    return fib_rec(n - 1) + fib_rec(n - 2)

@time_decorator
def fib_cicle(n):
    x0 = 0
    x1 = 1
    for i in range(n):
        x0, x1 = x1, x0+x1
    return x1

print(fib_rec(20)[1])
print(fib_cicle(30000)[1])

@time_decorator
@lru_cache(maxsize=None)
def fib_rec(n):
    if n == 0 or n == 1:
        return 1
    return fib_rec(n - 1) + fib_rec(n - 2)

@time_decorator
@lru_cache(maxsize=None)
def fib_cicle(n):
    x0 = 0
    x1 = 1
    for i in range(n):
        x0, x1 = x1, x0+x1
    return x1

print('А теперь с кэшем')
print(fib_rec(200)[1])
print(fib_cicle(30000)[1])