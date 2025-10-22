import sys
import collections


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    r, c, d = map(int, sys.stdin.readline().split())
    mp = []
    for _ in range(n):
        mp.append(list(map(int, sys.stdin.readline().split())) + [2])

    mp.append([2 for _ in range(m + 1)])

    # print(mp)

    cnt = 0
    q = collections.deque()
    q.append((r, c, d))

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    while len(q) > 0:
        _r, _c, _d = q.popleft()
        # print(_c, _r, _d, cnt, mp)

        if mp[_r][_c] == 0:
            mp[_r][_c] = -1
            cnt += 1

        for i in range(4):
            _nd = _d - i - 1
            if _nd < 0:
                _nd = _nd + 4

            if mp[_r + dy[_nd]][_c + dx[_nd]] == 0:   # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
                q.append((_r + dy[_nd], _c + dx[_nd], _nd))
                break
        else:  # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
            # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
            if mp[_r - dy[_d]][_c - dx[_d]] > 0:
                break
            q.append((_r - dy[_d], _c - dx[_d], _d))

    print(cnt)
