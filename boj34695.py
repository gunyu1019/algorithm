import collections
import sys


if __name__ == '__main__':
    k, n = map(int, sys.stdin.readline().split())
    s = []
    cnt = 0

    mod = int(1e9) + 7

    v = ord('a')
    dp = [0 for i in range(ord('a'), ord('z') + 1)]

    for _ in range(k):
        _s = sys.stdin.readline().strip()
        s.append(_s)
        dp[ord(_s[0]) - v] += 1

    cnt += sum(dp) % mod
    c_dp = dp[:]

    for _ in range(2, n):
        n_dp = [0 for i in range(ord('a'), ord('z') + 1)]
        
        for w in s:
            n_dp[ord(w[0]) - v] += c_dp[ord(w[1]) - v] % mod
            # print(w, c_dp[ord(w[0]) - v], w[0], w[1])

        cnt += sum(n_dp) % mod
        c_dp = n_dp[:]
        # print(_, cnt, n_dp, s)
    print(cnt % mod)
