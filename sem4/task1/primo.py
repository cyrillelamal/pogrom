# Разработать программу с реализацией функции для считывания json-
# данных из файла и вывод их в табличном виде на экран. Реализовать базовый
# синтаксис для обработки исключений (try .. except)
import json

FILE = "./composer.json"

f = None
try:
    f = open(FILE, "rt")
    obj = json.loads(f.read())  # type: dict
    print("|\t Ключ \t|\t Значение \t|")
    for k, v in obj.items():
        print(f"|\t{k}\t|\t{v}\t|")
except FileNotFoundError:
    print(f"{FILE} not found")
except json.JSONDecodeError:
    print(f"invalid JSON")
finally:
    if f is not None:
        f.close()
