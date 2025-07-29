def a(m, n):
    res = 1
    for i in range(m, m - n, -1):
        res *= i
    return res


def c(m, n):
    return int(a(m, n) / a(n, n))
