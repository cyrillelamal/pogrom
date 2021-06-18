class Fibonacci:
    def __init__(self):
        self._a = 0
        self._b = 1

    def __iter__(self):
        return self

    def __next__(self):
        nth = self._a + self._b
        self._a = self._b
        self._b = nth

        return nth
