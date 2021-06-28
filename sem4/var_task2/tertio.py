# Разработка функции-декоратора, вычисляющей время выполнения
# декорируемой функции.
import functools
import time


def measure(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time_ns()
        res = func(*args, **kwargs)
        end = time.time_ns()
        print(f'{end - start} ns')
        return res
    return wrapper
