import collections
import sys


if __name__ == '__main__':
    n, m, x = map(int, sys.stdin.readline().split())
    routes = [dict() for _ in range(n)]
    for _ in range(m):
        s, e, t = map(int, sys.stdin.readline().split())
        routes[s - 1][e - 1] = t
        # routes[e - 1][s - 1] = t

    hours = []
    for _s in range(n):
        if _s == x - 1:
            continue

        q = collections.deque()
        q.append((_s, 0))

        min_time1 = 0x7fffffff
        while len(q) > 0:
            _p, _t = q.popleft()
            if min_time1 < _t:
                continue

            if _p == x - 1:
                min_time1 = min(min_time1, _t)
                continue

            for _np, _nt in routes[_p].items():
                if _t + _nt < min_time1:
                    q.append((_np, _t + _nt))

        min_time2 = 0x7fffffff
        q.append((x - 1, 0))


        while len(q) > 0:
            _p, _t = q.popleft()
            if min_time2 < _t:
                continue

            if _p == _s:
                min_time2 = min(min_time2, _t)
                continue

            for _np, _nt in routes[_p].items():
                if _t + _nt < min_time2:
                    q.append((_np, _t + _nt))
        # print(min_time1, min_time2, _s)

        hours.append(min_time1 + min_time2)
    print(max(hours))
