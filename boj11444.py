import sys


m = dict()


def fibo(_n: int):
    if _n == 0:
        return 1
    elif _n == 1 or _n == 2:
        return 1

    if _n in m.keys():
        return m[_n]

    if _n % 2 == 0:
        result1 = fibo(_n // 2 - 1)
        result2 = fibo(_n // 2)
        m[_n] = ((2 * result1 + result2) * result2) % 1000000007
        return m[_n]
    m[_n] = (fibo((_n + 1) // 2) ** 2 + fibo((_n + 1) // 2 - 1) ** 2) % 1000000007
    return m[_n]


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    print(fibo(n))
