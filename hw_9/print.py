import csv
import time

def time_decorator(func):
    def wrapper(*args, **kwargs):

        start_time = time.time()
        res = func(*args, **kwargs)
        length_time = time.time() - start_time
        print('time '+str(length_time))
        return res
    return wrapper


def simple_multiple(coord):
    global matrix_1
    global matrix_2
    global kv_row1
    result = 0
    for i in range(kv_row1):
        result += matrix_1[coord[0]][i] * matrix_2[i][coord[1]]
    return result


matrix_1 = []
matrix_2 = []
with open("matrix_1.csv", encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter = ";")
    for row in file_reader:
        matrix_1.append(list(map(int, row)))
with open("matrix_2.csv", encoding='utf-8') as l_file:
    file_reader = csv.reader(l_file, delimiter = ";")
    for row in file_reader:
        matrix_2.append(list(map(int, row)))
kv_str1 = len(matrix_1)
kv_row1 = len(matrix_1[0])
kv_ctr2 = len(matrix_2[0])

@time_decorator
def main_function():
    global kv_str1, kv_ctr2
    res = [simple_multiple((i, j)) for i in range(kv_str1) for j in range(kv_ctr2 )]
    for i in range(kv_str1):
        print([res[i * kv_ctr2  + j] for j in range(kv_ctr2 )])


main_function()