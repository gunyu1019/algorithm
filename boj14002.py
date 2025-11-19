import sys


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))

    s = [1 for _ in range(n)]
    parent = [i for i in range(n)]
    for i, _a in enumerate(a):
        for j, _b in enumerate(a[:i]):
            if _a <= _b or s[i] >= s[j] + 1:
                continue

            s[i] = s[j] + 1
            parent[i] = j

    m_max = 0
    m_index = 0
    for i in range(n):
        if s[i] <= m_max:
            continue

        m_max = s[i]
        m_index = i

    print(m_max)

    check = [False for _ in range(n)]
    while m_index != parent[m_index]:
        check[m_index] = True
        m_index = parent[m_index]
    check[m_index] = True

    for i in range(n):
        if not check[i]:
            continue

        print(a[i], end=' ')
