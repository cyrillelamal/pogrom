# Разработать программу, позволяющую решать систему уравнений.
# Программа должна позволять вводить коэффициенты при неизвестных, а
# также должна учитывать возможность несовместного решения системы.
# Графический интерфейс реализовать с помощью PyQt или TKinter. Требуется
# протестировать программу с помощью библиотеки. Сформировать отчет по
# выполненной самостоятельной работе и опубликовать его в портфолио.
import unittest
import tkinter as tk
from tkinter import messagebox

import numpy as np

window = tk.Tk()
rows = []


def resolve(m, v):
    return np.linalg.solve(np.array(m), np.array(v))


def parse_nums(inp: str) -> list:
    inp = inp.strip()

    if not inp:
        return []

    return [
        float(e.strip())
        for e in filter(lambda c: c, inp.split(" "))
    ]


def add_row():
    row = tk.Entry(window)
    rows.append(row)
    row.pack()


def calc():
    m = []
    v = []
    try:
        for entry in rows:  # type: tk.Entry
            inp = entry.get()  # type: str
            coefficients = parse_nums(inp)
            if not coefficients:
                continue

            m.append(coefficients[:-1])
            v.append(coefficients[-1])

        res = resolve(m, v)
        messagebox.showinfo(title="Результат", message=str(res))
    except ValueError:
        messagebox.showerror(title="ОшибОЧКА", message="Введенные значения не похожи на цифры")
    except np.linalg.LinAlgError:
        messagebox.showerror(title="ОшибОЧКА", message="Несовместное решение")


if __name__ == "__main__":
    window.title('Решение систем линейных уравнений')

    calc_btn = tk.Button(window, text="Вычислить", command=calc)
    add_row_btn = tk.Button(window, text="Добавить уравнение", command=add_row)

    calc_btn.pack()
    add_row_btn.pack()

    window.mainloop()


class TestResolve(unittest.TestCase):
    def test_resolve(self):
        m = [
            [2, 5],
            [1, -10],
        ]
        v = [
            1,
            3,
        ]

        res = resolve(m, v)
        self.assertEqual(round(res[0], 0), 1)
        self.assertEqual(round(res[1], 1), -0.2)

    def test_parse_correct_nums(self):
        inp = "2 5 1"
        self.assertEqual(parse_nums(inp), [2, 5, 1])

        inp = " 2    5 1    "
        self.assertEqual(parse_nums(inp), [2, 5, 1])

        inp = " 2.3    -5  -11    "
        self.assertEqual(parse_nums(inp), [2.3, -5.0, -11.0])

    def test_parse_invalid_nums(self):
        inp = " sds2.3   5  -11    "
        self.assertRaises(ValueError, parse_nums, inp)
