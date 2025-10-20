import collections
import sys


def more_deepcopy(_board: list[list[int]]) -> list[list[int]]:
    _new_board = []
    for __board in _board:
        _new_board.append(__board[:])
    return _new_board


class Point:
    def __init__(self, y, x, t: str | None):
        self.x = x
        self.y = y
        self.t = t

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    b: list[list[int]] = [[] for _ in range(n)]

    op = Point(-1, -1, "o")
    rp = Point(-1, -1, "r")
    bp = Point(-1, -1, "b")

    for i in range(n):
        for j, w in enumerate(sys.stdin.readline().rstrip()):
            if w == "#":
                b[i].append(1)
            elif w == ".":
                b[i].append(0)
            elif w == "O":
                op = Point(i, j, "o")
                b[i].append(3)
            elif w == "R":
                rp = Point(i, j, "r")
                b[i].append(2)
            elif w == "B":
                bp = Point(i, j, "b")
                b[i].append(2)

    q = collections.deque()
    q.append((0, b, rp, bp))

    while len(q) > 0:
        _c, _b, _rp, _bp = q.popleft()
        # print(_c, _b, _bp == op, _rp == op, _rp.x, _rp.y, _bp.x, _bp.y, op.x, op.y)
        if _c > 10:
            continue
        if _bp == op or _rp == op:
            if _rp == op and _bp != op:
                print(_c)
                sys.exit(0)
            continue

        left_new_position = sorted([_rp, _bp], key=lambda p: p.x)
        top_new_position = sorted([_rp, _bp], key=lambda p: p.y)

        right_new_position = left_new_position.copy()
        down_new_position = top_new_position.copy()
        right_new_position.reverse()
        down_new_position.reverse()

        left_position = left_new_position.copy()
        top_position = top_new_position.copy()
        right_position = right_new_position.copy()
        down_position = down_new_position.copy()

        left_b = more_deepcopy(_b)
        right_b = more_deepcopy(_b)
        top_b = more_deepcopy(_b)
        down_b = more_deepcopy(_b)

        # print(_c, top_new_position[0].t, top_new_position[1].t, _rp.y, _bp.y)

        for j in range(2):
            left_d, right_d = False, False
            re = right_position[j]
            le = left_position[j]

            for i in range(1, m + 1):

                if not right_d and re.x + i < m and right_b[re.y][re.x + i] > 0:
                    right_b[re.y][re.x] = 0
                    if right_b[re.y][re.x + i] == 3:
                        right_new_position[j] = Point(re.y, re.x + i, re.t)
                    else:
                        right_b[re.y][re.x + i - 1] = 2
                        right_new_position[j] = Point(re.y, re.x + i - 1, re.t)
                    right_d = True
                # print(_c, left_b[e.y][e.x - i], left_d, e.x - i)
                if not left_d and le.x - i >= 0 and left_b[le.y][le.x - i] > 0:
                    left_b[le.y][le.x] = 0
                    if left_b[le.y][le.x - i] == 3:
                        left_new_position[j] = Point(le.y, le.x - i, le.t)
                    else:
                        left_b[le.y][le.x - i + 1] = 2
                        left_new_position[j] = Point(le.y, le.x - i + 1, le.t)
                    left_d = True

            top_d, down_d = False, False
            te = top_position[j]
            de = down_position[j]

            for i in range(1, n):
                if not down_d and de.y + i < n and down_b[de.y + i][de.x] > 0:
                    down_b[de.y][de.x] = 0
                    if down_b[de.y + i][de.x] == 3:
                        down_new_position[j] = Point(de.y + i, de.x, de.t)
                    else:
                        down_b[de.y + i - 1][de.x] = 2
                        down_new_position[j] = Point(de.y + i - 1, de.x, de.t)
                    down_d = True
                if not top_d and te.y - i >= 0 and top_b[te.y - i][te.x] > 0:
                    top_b[te.y][te.x] = 0
                    if top_b[te.y - i][te.x] == 3:
                        top_new_position[j] = Point(te.y - i, te.x, te.t)
                    else:
                        top_b[te.y - i + 1][te.x] = 2
                        top_new_position[j] = Point(te.y - i + 1, te.x, te.t)
                    top_d = True

        if left_new_position != left_position:
            _lrp = [element for element in left_new_position if element.t == "r"][0]
            _lbp = [element for element in left_new_position if element.t == "b"][0]
            q.append((_c + 1, left_b, _lrp, _lbp))
        if right_new_position != right_position:
            _rrp = [element for element in right_new_position if element.t == "r"][0]
            _rbp = [element for element in right_new_position if element.t == "b"][0]
            q.append((_c + 1, right_b, _rrp, _rbp))
        if top_new_position != top_position:
            _trp = [element for element in top_new_position if element.t == "r"][0]
            _tbp = [element for element in top_new_position if element.t == "b"][0]
            q.append((_c + 1, top_b, _trp, _tbp))
        if down_new_position != down_position:
            _drp = [element for element in down_new_position if element.t == "r"][0]
            _dbp = [element for element in down_new_position if element.t == "b"][0]
            q.append((_c + 1, down_b, _drp, _dbp))

    print(-1)
