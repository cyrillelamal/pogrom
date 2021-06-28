# Рефакторинг (модификация) программы с декоратором модулем functools
# и использование его функционала
import functools


FILE = "./log.txt"


def logger(func):
    @functools.wraps(func)
    def calc_with_log(*args, **kwargs):
        res = func(*args, **kwargs)
        with open(FILE, "at") as f:
            operator, a, b = args
            f.write(f"{a} {operator} {b} = {res}\n")

    return calc_with_log


@logger
def calc(operator, a, b) -> float:
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    else:
        raise Exception
