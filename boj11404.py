import collections
import sys


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())

    bus_route = [dict() for _ in range(n)]
    distance = [[0x7fffffff for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().strip().split())
        distance[a-1][b-1] = min(c, distance[a-1][b-1])

    for i in range(n):
        for j in range(n):
            for k in range(n):
                distance[j][k] = min(distance[j][i] + distance[i][k], distance[j][k])

    for i in range(n):
        distance[i][i] = 0

    for i in range(n):
        for j in range(n):
            if distance[i][j] == 0x7fffffff:
                print(0, end=" ")
                continue
            print(distance[i][j], end=" ")
        print()
