# Создание программы по распределению списка с случайными значениями
# на два списка по определенному критерию (четность/нечетность,
# положительные/отрицательные числа).
from sem4.task4.primo import fill


def partition(func, lst):
    a, b = [], []

    for e in lst:
        if func(e):
            a.append(e)
        else:
            b.append(e)

    return a, b


arr = fill(100)
odds, pairs = partition(lambda e: e & 1, arr)
pos, neg = partition(lambda e: e < 0, arr)
