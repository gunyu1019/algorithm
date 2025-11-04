import sys


if __name__ == '__main__':
    c, n = map(int, sys.stdin.readline().split())  # 홍보할 수 있는 도시(고객의 수), 도시의 개수
    cities = []
    for _ in range(n):
        cc, cm = map(int, sys.stdin.readline().split())
        cities.append((cc, cm))  # 각 도시에서 홍보할 때 대는 비용과 그 비용으로 얻을 수 있는 고객의 수

    dp = [0]

    for i in range(c + 100):
        dp.append(0x7fffffff)

        for j in range(n):
            if i + 1 >= cities[j][1] and i - cities[j][1] >= 0:
                dp[i] = min(dp[i], dp[i - cities[j][1]] + cities[j][0])

    print(min(dp[c:]))
