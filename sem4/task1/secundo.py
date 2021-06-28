# Дополнение программы для считывания данных проверкой утверждений
# или высказываний (assert). Создание отдельного блока для такой проверки (с
# помощью __name__) и скрипта командной строки для запуска этих проверок.
import json

FILE = "./composer.json"


def print_json(path: str):
    f = None
    obj = None
    try:
        f = open(path, "rt")
        obj = json.loads(f.read())  # type: dict or None
        print("|\t Ключ \t|\t Значение \t|")
        for k, v in obj.items():
            print(f"|\t{k}\t|\t{v}\t|")
    except FileNotFoundError:
        print(f"{path} not found")
    except json.JSONDecodeError:
        print(f"invalid JSON")
    finally:
        if f is not None:
            f.close()
    return obj


if __name__ == "__main__":
    obj = print_json(FILE)
    assert obj is not None

    obj = print_json("foo.bar")
    assert obj is None
