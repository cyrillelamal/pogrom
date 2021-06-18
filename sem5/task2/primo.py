def fibonacci(limit: int):
    a, b = 0, 1
    seq = [a, b]
    while limit > 0:
        nth = a + b
        seq.append(nth)
        a = b
        b = nth
        limit -= 1

    return seq
