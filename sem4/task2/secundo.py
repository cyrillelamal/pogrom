# Дополнение программы «Калькулятор» декоратором, сохраняющий
# действия, которые выполняются в файл-журнал.
FILE = "./log.txt"


def logger(func):
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


calc('-', 1, 2)
calc('/', 13, 3)
