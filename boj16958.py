#!/usr/bin/python3
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
s = {}; l = {}

for i in range(n):
    _s, _e = map(int, sys.stdin.readline().split())
    l[_s] = _e

for i in range(m):
    _s, _e = map(int, sys.stdin.readline().split())
    s[_s] = _e    

# q = deque([(x + 2, 0) for x in range(6)])
q = deque([(1, 0)])
cnt = 0x7fffffff
visited = [0x7fffffff for _ in range(106)]
visited[0] = 1

while len(q) > 0:
    np, _cnt = q.popleft()
    if _cnt > cnt:
        continue
    print(_cnt, np)        
    if np == 100:
        cnt = min(cnt, _cnt)
        
    if np in s.keys():
        q.append((s[np], _cnt))
        continue
    if np in l.keys():
        q.append((l[np], _cnt))    
        continue
    
        
    for i in range(6):
        if np + i + 1 > 100 or visited[np + i] < _cnt:
            continue
        visited[np + i] = _cnt
        q.append((np + i + 1, _cnt + 1))    

print(cnt)
