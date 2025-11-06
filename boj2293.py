import sys


if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().split())
    m = []
    dp = [0 for _ in range(k + 1)]
    dp[0] = 1

    for _ in range(n):
        m.append(int(sys.stdin.readline()))
        # dp[m[-1]] = 1

    for i in m:
        for j in range(i, k + 1):
            dp[j] += dp[j - i]

    print(dp[-1])
