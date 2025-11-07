import sys


if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().split())

    m = []
    inf = 0x7fffffff
    dp = [inf for _ in range(k)]

    for _ in range(n):
        m.append(int(sys.stdin.readline()))
        if m[-1] - 1 > k:
            continue
        dp[m[-1] - 1] = 1

    for i in range(k + 1):
        for j in m:
            if i - j - 1 < 0:
                continue
            dp[i - 1] = min(dp[i - 1], dp[i - j - 1] + 1)

    # print(dp)
    if dp[-1] == inf:
        print(-1)
        sys.exit(0)
    print(dp[-1])
