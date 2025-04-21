def factorial_rec(x: int):
    if x == 0:
        return 1
    else:
        return x * factorial_rec(x - 1)


def factorial_loop(x: int):
    r = x
    for i in range(2, x):
        r *= i
    return r
