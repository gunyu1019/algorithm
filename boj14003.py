import sys


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))

    m_max = 0

    s = [(-1, -1) for _ in range(n)]
    parent = [(-1, -1) for _ in range(n)]

    # Initialization
    s[0] = (0, a[0])
    m_max += 1

    for i in range(1, n):
        # for j, _b in enumerate(a[:i]):
        #     if _a <= _b or s[i] >= s[j] + 1:
        #         continue

        #     s[i] = s[j] + 1

        #     parent[i] = j
        # print(a[i], s)
        if s[m_max - 1][1] < a[i]:
            parent[i] = s[m_max - 1]
            s[m_max] = (i, a[i])
            m_max += 1
            continue

        start_position = 0
        end_position = m_max - 1
        while start_position <= end_position:
            mid_position = (start_position + end_position) // 2
            if s[mid_position][1] < a[i]:
                start_position = mid_position + 1
            elif s[mid_position][1] > a[i]:
                end_position = mid_position - 1
            else:  # SAME
                break

        position = (start_position + end_position) // 2
        if s[position][1] == a[i]:
            continue
        position += 1
        # print(i, position, start_position, end_position, a[i], s)
        if position < 0:
            position = 0
        parent[i] = s[position - 1] if position > 0 else (-1, a[i])
        s[position] = (i, a[i])

    print(m_max)

    m_index = s[m_max - 1][0]
    check = [False for _ in range(n)]
    while m_index != -1:
        check[m_index] = True
        m_index = parent[m_index][0]

    # print(s)
    # print(parent)
    # print(check)

    for i in range(n):
        if not check[i]:
            continue

        print(a[i], end=' ')
