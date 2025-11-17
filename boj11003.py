import collections
import sys


if __name__ == '__main__':
    n, l = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))

    q = collections.deque()
    q.append(0)
    print(a[0], end=" ")

    for i in range(1, n):

        # 1. A(i - l + 1) ~ Ai 사이 값
        p = i - l + 1 if i - l + 1 >= 0 else 0
        while len(q) > 0 and (q[0] < p or a[q[0]] > a[i]):
            q.popleft()
            # (q, a[i], q[0], q[0] < p, a[q[0]] > a[i], a[q[0]])

        # print(q, a[i], i, a[q[0]])
        if len(q) > 0:
            print(a[q[0]], end=" ")
        else:
            print(a[i], end=" ")

        # 2. q[-1] 위치의 a가 현 a보다 작은가?
        while len(q) > 0 and a[q[-1]] > a[i]:
            q.pop()

        q.append(i)
