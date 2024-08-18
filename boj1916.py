import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
node = [[] for k in range(n)]

for i in range(m):
   bs, be, t = map(int, sys.stdin.readline().split())
   
   node[bs-1].append((t, be)) # 시간, 목적지
   
s, e = map(int, sys.stdin.readline().split())    
q = deque([(s, 0, None)])
cnt = [0x7fffffff for _ in range(n)]

while len(q) > 0: 
    np, t, pp = q.popleft()
    if np == e or cnt[np] < t:
        continue

    for nt, dest in node[np-1]:
        if t + nt > cnt[dest-1] or pp == dest:
            continue
        cnt[dest-1] = t + nt    
        q.append((dest, t + nt, np))
 
print(cnt[e-1]) 
