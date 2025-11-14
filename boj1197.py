import collections
import sys


if __name__ == "__main__":
    v, e = map(int, sys.stdin.readline().split())
    route = []

    for _ in range(e):
        _a, _b, _c = map(int, sys.stdin.readline().split())
        route.append((_a - 1, _b - 1, _c))

    route.sort(key=lambda x: x[2])
    # print(route)

    parents = [_ for _ in range(v)]

    sums = 0
    cnt = 0
    for _a, _b, _c in route:
        if cnt >= v - 1:
            break

        z1 = _a
        while parents[z1] != z1:
            z1 = parents[z1]

        z2 = _b
        while parents[z2] != z2:
            z2 = parents[z2]

        if z1 == z2:
            continue

        if z1 >= z2:
            parents[z2] = z1
        else:
            parents[z1] = z2

        sums += _c
        cnt += 1

    # print(parents)
    print(sums)
