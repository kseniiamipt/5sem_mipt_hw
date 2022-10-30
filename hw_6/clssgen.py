a = list()


def squares():
    res = 0
    while True:
        yield res**2
        res += 1
        if res > 100:
            return


print(squares())


def my_range(start, finish=None, step=1):
    if step == 0:
        raise ValueError
    if finish is None:
        start, finish = 0, start
    yield start
    while (finish - start) * (finish - start - step) > 0:
        start += step
        yield start


for i in my_range(4, 1, -1):
    print(i)

print()

for i in squares():
    print(i)
    if i > 10000:
        break