import sys


if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().split())
    s = []

    for i in range(n):
        w, v = map(int, sys.stdin.readline().split())
        s.append((w, v))

    dp = []
    items = [[] for _ in range(k)]
    for i in range(k):
        dp.append(0)

        for j in range(n):
            if i - s[j][0] < 0:
                pre_v = 0
            else:
                pre_v = dp[i - s[j][0]]

            if i + 1 >= s[j][0] and dp[i] < pre_v + s[j][1] and j not in items[i - s[j][0]]:
                if i - s[j][0] < 0:
                    dp[i] = s[j][1]
                    items[i] = [j]
                else:
                    dp[i] = pre_v + s[j][1]
                    items[i] = items[i - s[j][0]] + [j]

        # print(i + 1, dp, items)

    print(max(dp))
