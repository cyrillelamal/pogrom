# Дополнение программы для считывания данных с использованием
# менеджера контекстов и реализации расширенного синтаксиса для обработки
# исключений.
import json

FILE = "./composer.json"


def print_json(path: str):
    obj = None

    try:
        with open(path, "rt") as f:
            obj = json.loads(f.read())  # type: dict or None
            print("|\t Ключ \t|\t Значение \t|")
            for k, v in obj.items():
                print(f"|\t{k}\t|\t{v}\t|")
    except FileNotFoundError:
        print(f"{path} not found")
    except json.JSONDecodeError:
        print(f"invalid JSON")
    finally:
        print(f"file is already closed")
    return obj


if __name__ == "__main__":
    obj = print_json(FILE)
    assert obj is not None

    obj = print_json("foo.bar")
    assert obj is None
