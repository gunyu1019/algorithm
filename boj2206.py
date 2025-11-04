import collections
import sys


if __name__ == '__main__':
    a = []
    n, m = map(int, sys.stdin.readline().split())
    for _ in range(n):
        a.append([int(w) for w in sys.stdin.readline().strip()])

    tt = [[[0x7fffffff, 0x7fffffff] for _ in range(m)] for _ in range(n)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    q = collections.deque()
    q.append((0, 0, False, 1))

    mm = 0x7fffffff

    while len(q) > 0:
        x, y, broken_wall, t = q.popleft()

        if x == n - 1 and y == m - 1:
            mm = min(mm, t)
            break

        for i in range(4):
            if not (0 <= x + dx[i] < n and 0 <= y + dy[i] < m):
                continue
            # print(x + dx[i], y + dy[i], n, m)

            if a[x + dx[i]][y + dy[i]] == 0 and tt[x + dx[i]][y + dy[i]][broken_wall] > t + 1:
                tt[x + dx[i]][y + dy[i]][broken_wall] = t + 1
                q.append((x + dx[i], y + dy[i], broken_wall, t + 1))
            elif a[x + dx[i]][y + dy[i]] == 1 and not broken_wall and tt[x + dx[i]][y + dy[i]][broken_wall] > t + 1:
                tt[x + dx[i]][y + dy[i]][1] = t + 1
                q.append((x + dx[i], y + dy[i], True, t + 1))

    if mm == 0x7fffffff:
        print(-1)
        sys.exit(0)
    print(mm)
