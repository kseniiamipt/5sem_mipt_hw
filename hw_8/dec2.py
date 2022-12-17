def printagrs_decorator(func):
    def wrapper(*args):
        res = func(*args)
        print(*args)
        return res
    return wrapper


@printagrs_decorator
def foo(*x):
    print('helloo')

foo(334,24,657)