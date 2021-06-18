# Разработать программу, позволяющую решать квадратное уравнение
# через вычисление дискриминанта. В программе должен быть предусмотрен
# ввод значений коэффициентов a, b, c пользователем. Требуется
# протестировать программу с помощью одной из специальных библиотек.
# Сформировать отчет по выполненной самостоятельной работе и
# опубликовать его в портфолио.
import math
import unittest


def quadratic_roots(a, b, c) -> tuple:
    d = b * b - 4 * a * c

    if d < 0:
        return None, None

    sqrt = math.sqrt(d)
    divisor = 2 * a

    return (-b + sqrt) / divisor, (-b - sqrt) / divisor


class TestQuadratic(unittest.TestCase):
    def test_negative_sqrt(self):
        a = c = 100
        b = 1

        res = quadratic_roots(a, b, c)
        self.assertEqual((None, None), res)

    def test_positive_sqrt(self):
        a = -1
        b = 100
        c = 64

        res = quadratic_roots(a, b, c)
        self.assertIsNotNone(res[0])
        self.assertIsNotNone(res[1])
