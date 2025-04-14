import random
import typing
import timeit
import functools
import matplotlib.pyplot as plt
import numpy as np


def timing_decorator(ndigits: int, number: int, setup: str) -> typing.Callable:
    def decorator(func: typing.Callable) -> typing.Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> float:
            usage_time = timeit.timeit(
                lambda: func(*args, **kwargs),
                globals=globals(),
                setup=setup,
                number=number,
            )
            return round(usage_time / number, ndigits)

        return wrapper

    return decorator



max_n = 10000


matrix_size = (max_n, max_n)
matrix_a = np.random.rand(*matrix_size)
matrix_b = np.random.rand(*matrix_size)

n_values = list(range(1, max_n, 1300))
average_times = []


@timing_decorator(6, 5, "import numpy as np")
def post_f(matrix_a, matrix_b):
    result = np.dot(matrix_a, matrix_b)
    return result


for n in n_values:
    print(n)
    average_time = post_f(matrix_a[:n, :n], matrix_b[:n, :n])
    average_times.append(average_time)

plt.plot(n_values, average_times, linestyle='-', color='b')

plt.title('Зависимость среднего времени выполнения от n \n (от матричного произведения)')
plt.xlabel('n')
plt.ylabel('Среднее время выполнения (секунды)')
plt.savefig('2.png')