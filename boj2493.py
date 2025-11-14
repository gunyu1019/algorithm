import sys


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    q = list(map(int, sys.stdin.readline().rstrip().split()))
    r = ["0" for _ in range(n)]

    for i in range(n - 1, -1 , -1):
        for j in range(i - 1, -1, -1):
            # print(q[i], q[j], end=" ")
            if q[i] <= q[j]:
                r[i] = str(j + 1)
                break
        # print()
    print(" ".join(r))
