import sys

n = int(sys.stdin.readline())
l = []

for _ in range(n):
    l.append(
        list(
            map(int, sys.stdin.readline().split())
        )
    )
    
result1 = [l[0][i] for i in range(3)]
result2 = [l[0][i] for i in range(3)]

for i in range(1, n):
    result1 = [
        l[i][0]+max(result1[0], result1[1]),
        l[i][1]+max(result1[0], result1[1], result1[2]),
        l[i][2]+max(result1[1], result1[2])
    ]
    result2 = [
        l[i][0]+min(result2[0], result2[1]),
        l[i][1]+min(result2[0], result2[1], result2[2]),
        l[i][2]+min(result2[1], result2[2])
    ]
    
result1.sort()
result2.sort()    
print(result1[-1], result2[0])   
