import sys


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    cable = []
    for _ in range(n):
        _s, _e = map(int, sys.stdin.readline().split())
        cable.append([_s, _e])

    cable.sort(key=lambda x: x[0])
    dp = [1 for _ in range(n)]
    parents = [i for i in range(n)]

    for i, _ in enumerate(cable):
        for j in range(i):
            if cable[j][1] >= cable[i][1]:
                continue

            if dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parents[i] = j

    m_max = 0
    m_index = 0
    for i in range(n):
        if m_max >= dp[i]:
            continue

        m_max = dp[i]
        m_index = i

    check = [False for _ in range(n)]
    while m_index != parents[m_index]:
        check[m_index] = True
        m_index = parents[m_index]
    check[m_index] = True

    # print(check, parents, dp)

    sys.stdout.write(str(n - m_max) + "\n")
    for i, condition in enumerate(check):
        if condition:
            continue

        sys.stdout.write(str(cable[i][0]) + "\n")
