import sys


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    m = list(map(int, sys.stdin.readline().split()))

    dp0 = [m[0]]
    dp1 = [m[0]]
    for i in range(1, n):
        dp0.append(max(m[i] + dp0[-1], m[i]))
        dp1.append(max(dp0[-2], dp1[-1] + m[i]))

    print(max(max(dp0), max(dp1)))
