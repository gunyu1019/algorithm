import sys

sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
node = [[] for _ in range(n)]
visited = [False for _ in range(n)]
cnt = -1
for _ in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    a.pop(-1)
    for i in range(1, len(a), 2):
        # print(a[0], a[i], a[i+1])
        node[a[0]-1].append((a[i]-1, a[i+1]))


def dfs(p, c):
    global cnt
    if len(node[p]) == 0:
        return c
    
    result = []
    for dest, cost in node[p]:
        if visited[dest]:
            continue
        visited[dest] = True    
        result.append(
            dfs(dest, cost)
        )
    result = sorted(result)    
    if len(result) == 0:
        return c
    # print(result, p, c)
    if len(result) > 1:
        cnt = max(result[-1] + result[-2], cnt)
    return result[-1] + c  

visited[0] = True
cnt = max(dfs(0, 0), cnt)
print(cnt)
