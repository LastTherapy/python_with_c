import time
from itertools import tee
from matrix import mul as c_mul

def timeit_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Засекаем время перед выполнением функции
        result = func(*args, **kwargs)  # Вызываем функцию
        end_time = time.time()  # Засекаем время после выполнения функции
        print(f"Время выполнения {func.__name__}: {end_time - start_time} секунд")
        return result
    return wrapper


@timeit_decorator
def python_mul(a, b):
    b_iter = tee(zip(*b), len(a))
    return [
        [
            sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b))
            for col_b in b_iter[i]
        ] for i, row_a in enumerate(a)
    ]

decorated_c_mul = timeit_decorator(c_mul)


x = [[i + j * 10 for i in range(1, 31)] for j in range(40)]  # 40 строк, 30 столбцов
y = [[i + j * 5 for i in range(1, 21)] for j in range(30)]

python_mul(x, y)
decorated_c_mul(x, y)

