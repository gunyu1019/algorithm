import collections
import sys


if __name__ == '__main__':
    t = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        p, n = map(int, sys.stdin.readline().rstrip().split())

        a = []
        total_sum = 0
        min_value = int(1e9)

        # 실제 지불한 값
        flow_amount = [0 for _ in range(n)]

        for _i, _a in enumerate(sys.stdin.readline().rstrip().split()):
            a.append([int(_a), _i])
            total_sum += a[-1][0]
            flow_amount[_i] = min(p // n, a[-1][0])

        if total_sum < p:
            print("IMPOSSIBLE")
            continue
        elif sum(flow_amount) == p:
            print(" ".join(map(str, flow_amount)))
            continue

        a.sort(key=lambda x: x[0], reverse=True)
        q = collections.deque()
        p -= sum(flow_amount)

        for _a, _i in a:
            if flow_amount[_i] < _a:
                q.append((_i, _a - flow_amount[_i]))

        while p > 0 and len(q) > 0:
            _i, remaining_amount = q.popleft()
            if remaining_amount <= 0:
                continue

            flow_amount[_i] += 1
            remaining_amount -= 1
            p -= 1

            if remaining_amount > 0:
                q.append((_i, remaining_amount))

        print(" ".join(map(str, flow_amount)))
