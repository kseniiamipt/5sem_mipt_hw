def fib_n(n):
    if n == 0:
        return 0
    n_1 = 0
    n_2 = 1
    for i in range(n-1):
        n_1_p = n_1
        n_1 = n_2
        n_2 = n_2 + n_1_p
    return n_2
# print(fib_n(9))