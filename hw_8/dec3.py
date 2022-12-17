def try_error_decorator(func):
    def wrapper(*arg):
        try:
            res = func(*arg)
            return res
        except Exception:
            print('Error')
    return wrapper


@try_error_decorator
def foo(x):
    print(x / 87)

foo(345)
foo('sdsd')