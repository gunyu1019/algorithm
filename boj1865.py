import sys
import collections


if __name__ == '__main__':
    tc = int(sys.stdin.readline())
    for _ in range(tc):
        n, m, w = map(int, sys.stdin.readline().split())

        road = []

        for _ in range(m):
            _s, _e, _t = map(int, sys.stdin.readline().split())
            road.append((_s - 1, _e - 1, _t))
            road.append((_e - 1, _s - 1, _t))

        for _ in range(w):
            _s, _e, _t = map(int, sys.stdin.readline().split())
            road.append((_s - 1, _e - 1, -_t))

        d = [0x7fffffff for _ in range(n)]
        d[0] = 0

        for i in range(n - 1):
            for s, e, t in road:
                if d[s] + t < d[e]:
                    d[e] = d[s] + t

        for s, e, t in road:
            if d[s] + t < d[e]:
                print("YES")
                break
        else:
            print("NO")
