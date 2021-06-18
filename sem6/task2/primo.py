# На основе кода, предоставленного преподавателем, реализовать генератор
# чисел ряда Фибоначчи. Генератор требуется создать двумя вариантами: с
# помощью генератора списков, с помощью функции, внутри которой yield.

END = 10

fibonacci = [0, 1]
fibonacci += [
    (fibonacci := [fibonacci[1], fibonacci[0] + fibonacci[1]]) and fibonacci[1]
    for k in range(END)
]


def fibonacci_func():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
