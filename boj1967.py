import sys

sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
node = [[] for _ in range(n)]
cnt = -1
for _ in range(n-1):
    s, e, d = map(int, sys.stdin.readline().split())
    node[s-1].append((e-1, d))


def dfs(p, c):
    global cnt
    if len(node[p]) == 0:
        return c
    
    result = []
    for dest, cost in node[p]:
        result.append(
            dfs(dest, cost)
        )
    result = sorted(result)    
    # print(result, p, c)
    if len(result) > 1:
        cnt = max(result[-1] + result[-2], cnt)
    return result[-1] + c  

cnt = max(dfs(0, 0), cnt)
print(cnt)
