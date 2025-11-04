import sys


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    route = []

    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        route.append((a-1, b-1, c))

    inf = 0x7fffffff
    d = [inf for _ in range(n)]
    d[0] = 0

    for i in range(n - 1):
        for s, e, t in route:
            if d[s] != inf and d[s] + t < d[e]:
                d[e] = d[s] + t

    for s, e, t in route:
        if d[s] != inf and d[s] + t < d[e]:
            print('-1')
            sys.exit(0)

    for _d in d[1:]:
        if _d == inf:
            print('-1')
            continue
        print(_d)
