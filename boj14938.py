import sys


if __name__ == '__main__':
    n, m, r = map(int, sys.stdin.readline().split())
    t = list(map(int, sys.stdin.readline().split()))

    distance = [[0x7fffffff for _ in range(n)] for _ in range(n)]
    for i in range(r):
        _a, _b, _c = map(int, sys.stdin.readline().split())
        distance[_a - 1][_b - 1] = _c
        distance[_b - 1][_a - 1] = _c

    for i in range(n):
        distance[i][i] = 0
        for j in range(n):
            for k in range(n):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    result = [0 for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if distance[i][j] > m:
                continue
            result[i] += t[j]
    # print(result, distance)
    print(max(result))
