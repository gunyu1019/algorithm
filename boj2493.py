import collections
import sys


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    q = list(map(int, sys.stdin.readline().rstrip().split()))
    r = [0 for _ in range(n)]

    stack = collections.deque()

    for i in range(n - 1, -1 , -1):
        while len(stack) > 0 and stack[-1][0] <= q[i]:
            r[stack[-1][1]] = i + 1
            stack.pop()
        stack.append((q[i], i))

    print(" ".join(map(str, r)))
