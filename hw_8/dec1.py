def reverse_decorator(func):
    def wrapper(*args):
        arg_list = list(args)
        arg_list.reverse()
        res = func(*arg_list)
        return res
    return wrapper


@reverse_decorator
def foo(*x):
    print(x)

foo(1, 6, 8, 9, 0)