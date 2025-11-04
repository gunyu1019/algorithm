import collections
import sys


if __name__ == '__main__':
    t = int(sys.stdin.readline())
    for _ in range(t):
        n,k = map(int, sys.stdin.readline().split())
        d = list(map(int, sys.stdin.readline().split()))

        routes: list[list[int]] = [[] for _ in range(n)]
        reverse_routes: list[list[int]] = [[] for _ in range(n)]
        time = [-1 for _ in range(n)]
        for _ in range(k):
            _s, _e = map(int, sys.stdin.readline().split())
            routes[_s-1].append(_e-1)
            reverse_routes[_e-1].append(_s-1)
        w = int(sys.stdin.readline())

        q = collections.deque()
        q.append(w-1)
        time[w-1] = d[w-1]

        while len(q) > 0:
            p = q.popleft()

            for r in reverse_routes[p]:
                if r < 0:
                    continue

                if time[r] < time[p] + d[r]:
                    time[r] = time[p] + d[r]
                    q.append(r)
        print(max(time))
