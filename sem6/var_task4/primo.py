# Написать программу, в которой пользователь вводит число от 0 до 9
# включительно, а программа выводит название введённого числа, а если
# второй входной аргумент type имеет значение bin, oct, hex, то функция
# преобразует это число в бинарную, восьмеричную или шестнадцатеричную
# форму. Предусмотреть проверку корректности введённого пользователем
# значения. При реализации используемые библиотеки должны находиться в
# виртуальном окружении (использовать virtualenv).
import argparse

DIGITS = {
    0: "zero",
    1: "un",
    2: "deux",
    3: "trois",
    4: "quatre",
    5: "cinq",
    6: "six",
    7: "sept",
    8: "huit",
    9: "neuf",
}
TRANSFORMERS = {
    "bin": lambda d: "{0:b}".format(d),
    "oct": lambda d: "{0:o}".format(d),
    "hex": lambda d: "{0:x}".format(d),
}
SYSTEMS = list(TRANSFORMERS.keys())

parser = argparse.ArgumentParser(description="Информация о числах.")
parser.add_argument("digit", metavar='D', type=int, help="Число от 0 до 9 или, другими словами, цифра.")
parser.add_argument("--type", dest="digit_type", help=f"Система счисления {SYSTEMS}")

args = parser.parse_args()
digit = args.digit
digit_type = args.digit_type

if digit not in DIGITS:
    print(f"unexpected value \"{digit}\". The value must be in the range 1..9.")
    exit(1)
if digit_type is not None and digit_type not in TRANSFORMERS:
    print(f"Unexpected type \"{digit_type}\". Try to use the one of {SYSTEMS}")
    exit(1)

print(f"Вы ввели {digit}: {DIGITS[digit]}")
if digit_type:
    print(TRANSFORMERS[digit_type](digit))

exit(0)
