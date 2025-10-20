import sys


class TP:
    def __init__(self, t: int, p: int):
        self.t = t
        self.p = p


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    tp = []
    for _ in range(n):
        _t, _p = map(int, sys.stdin.readline().split())
        tp.append(TP(_t, _p))

    a: list[TP] = []
    for i in range(n):
        mp = 0
        for j in range(i):
            if a[j].t >= i + 1:
                continue
            mp = max(a[j].p, mp)

        a.append(TP(tp[i].t + i, tp[i].p + mp))

    sorted_a = sorted(a, key=lambda _tp: _tp.p)
    result = []
    for _tp in sorted_a:
        if _tp.t <= n:
            result.append(_tp)
    # print([i.p for i in sorted_a])
    # print([i.t for i in sorted_a])

    if len(result) == 0:
        print(0)
        sys.exit(0)
    print(result[-1].p)
