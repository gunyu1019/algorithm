import collections
import sys


sys.setrecursionlimit(10**9)


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    m = []
    for _ in range(n):
        l = list(sys.stdin.readline().rstrip())
        m.append(l)

    visited = [[False for _ in range(n)] for _ in range(n)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    q = collections.deque()

    def dfs(x, y, _m):
        if visited[x][y]:
            return
        visited[x][y] = True

        for i in range(4):
            if not (0 <= x + dx[i] < n and 0 <= y + dy[i] < n):
                continue

            if _m == "G" and m[x + dx[i]][y + dy[i]] == "R" or _m == "R" and m[x + dx[i]][y + dy[i]] == "G":
                q.append((x + dx[i], y + dy[i]))

            if visited[x + dx[i]][y + dy[i]] or m[x + dx[i]][y + dy[i]] != _m:
                continue
            dfs(x + dx[i], y + dy[i], _m)

    cnt0 = 0
    cnt1 = 0

    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            dfs(i, j, m[i][j])

            while len(q) > 0:
                x, y = q.popleft()
                if visited[x][y]:
                    continue
                dfs(x, y, m[x][y])
                cnt1 += 1
            cnt0 += 1

    print(cnt0 + cnt1, cnt0)
