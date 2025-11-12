import sys


if __name__ == '__main__':
    n, s = map(int, sys.stdin.readline().split())
    m = list(map(int, sys.stdin.readline().split()))

    sums = [0 for _ in range(n + 1)]
    for i in range(n):
        sums[i + 1] = sums[i] + m[i]

    inf = 0x7fffffff
    cnt = inf

    index1 = 0
    index2 = 0

    while index1 < n + 1 and index2 < n + 1:
        _sum = sums[index2] - sums[index1]
        # print(_sum)
        if _sum >= s:
            cnt = min(cnt, index2 - index1)
            index1 += 1
        else:
            index2 += 1

    if cnt == inf:
        print(0)
        sys.exit(0)
    sys.stdout.write(str(cnt))
