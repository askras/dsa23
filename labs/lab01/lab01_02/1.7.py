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
                setup=setup,
                number=number,
            )
            return round(usage_time / number, ndigits)

        return wrapper

    return decorator
max_n = 1800001
max_vector = [random.randint(1, 100) for _ in range(max_n)]

ndigits = 6
number_of_runs = 5

n_values = list(range(1, max_n, 1800))
average_times = []


@timing_decorator(ndigits, number_of_runs,"import numpy as np")
def calculate_average(vector):
    return sum(vector) / len(vector)


for n in n_values:
    print(n)

    average_time = calculate_average(max_vector[:n])
    average_times.append(average_time)

plt.plot(n_values, average_times, linestyle='-', color='b')
plt.title('Зависимость времени поиска среднего арифметического от n')
plt.xlabel('n')
plt.ylabel('Среднее время выполнения (секунды)')

plt.savefig('1.7.png')