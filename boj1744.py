import sys


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    m = []

    m1 = []
    m2 = []
    for _ in range(n):
        m.append(int(sys.stdin.readline()))
        if m[-1] > 0:
            m1.append(m[-1])
        else:
            m2.append(m[-1])

    s = sum(m)

    m1.sort(reverse=True)
    m2.sort()

    m3 = m1 + m2
    # print(m3)

    visited = [False for _ in range(n)]

    for i in range(n - 1):
        n1, n2 = m3[i], m3[i + 1]
        if s - n1 - n2 + n1 * n2 <= s or visited[i] or visited[i + 1]:
            continue
        visited[i] = visited[i + 1] = True
        s = s - n1 - n2 + n1 * n2
    print(s)


