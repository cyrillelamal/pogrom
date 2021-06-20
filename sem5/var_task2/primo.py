# Разработать функцию, возвращающую список чисел ряда Фибоначчи с
# использованием бесконечных итераторов (модуль itertools).
from itertools import cycle


def fibonacci(limit=100):
    default = limit
    a, b = 0, 1

    while b < limit:
        nth = a + b
        limit = yield nth
        limit = limit if limit is not None else default
        a = b
        b = nth


if __name__ == "__main__":
    gen = fibonacci()
    lazy = cycle(gen)
    for c in lazy:
        print(c)
