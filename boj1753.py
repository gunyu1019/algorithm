import sys
from queue import PriorityQueue
from collections import deque

n, m = map(int, sys.stdin.readline().split())  
s = int(sys.stdin.readline())  
cnt = [float('inf') for _ in range(n)]
r = [[] for _ in range(n)]

for _ in range(m):
    _s, _e, t = map(int, sys.stdin.readline().split())
    r[_s-1].append((_e-1, t))
    
q = PriorityQueue()
q.put((0, s-1))
cnt[s-1] = 0    
while q.qsize() > 0:
    t, np = q.get()
    if cnt[np] < t:
        continue
    for dest, nt in r[np]:
        # print(cnt[dest], dest, t, nt)
        if cnt[dest] <= t + nt:
            continue
        cnt[dest] = t + nt    
        q.put((t + nt, dest))

for t in cnt:
    if t == float('inf'):
        print("INF")
        continue
    print(t) 
