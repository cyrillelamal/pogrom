# Разработать прототип программы «Калькулятор», позволяющую
# выполнять базовые арифметические действия и функцию обертку,
# сохраняющую название выполняемой операции, аргументы и результат в
# файл
FILE = "./log.txt"


def logger(func):
    def calc_with_log(*args, **kwargs):
        res = func(*args, **kwargs)
        with open(FILE, "at") as f:
            operator, a, b = args
            f.write(f"{a} {operator} {b} = {res}\n")

    return calc_with_log


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


func = logger(calc)


func('+', 3, 5)
func('*', 2119, 21)
