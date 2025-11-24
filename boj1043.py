import collections
import sys


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().strip().split())
    a = [int(_a) - 1 for _a in sys.stdin.readline().strip().split()][1:]
    p = []

    route = [[] for _ in range(n)]
    visited = [False for _ in range(n)]
    for _ in range(m):
        _p = [int(__p) - 1 for __p in sys.stdin.readline().strip().split()][1:]
        if len(_p) == 0:
            continue

        p.append(_p)

        p_length = len(_p)
        for i in range(p_length):
            for j in range(p_length):
                if i == j:
                    continue

                route[_p[i]].append(_p[j])

    for i in a:
        if visited[i]:
            continue
        visited[i] = True

        q = collections.deque([i])

        while len(q) > 0:
            _p = q.popleft()
            for np in route[_p]:
                if not visited[np]:
                    visited[np] = True
                    q.append(np)
    # print(visited)
    cnt = 0
    for i in range(m):
        if visited[p[i][0]]:
            continue
        cnt += 1

    print(cnt)
