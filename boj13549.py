import sys
from collections import deque

s, e = map(int, sys.stdin.readline().split())    
q = deque([(s, 0)])
cnt = [-1 for _ in range(100002)]

while len(q) > 0: 
    np, t = q.popleft()
    if np > 100000 or np < 0 or 0 < cnt[np] < t:
        continue

    for nt, dest in [
        (0, np * 2),
        (1, np + 1),
        (1, np - 1)
    ]:
        if dest > 100000 or dest < 0:
            continue
        if 0 <= cnt[dest] <= t + nt:
            continue
        cnt[dest] = t + nt    
        q.append((dest, t + nt))
print(0 if s == e else cnt[e])        
