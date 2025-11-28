import sys


# 이 문제를 풀며 사용한 알고리즘: LCS (이분탐색), 백트래킹, DP
if __name__ == '__main__':
    n = int(sys.stdin.readline())
    present = []
    for _ in range(n):
        _a, _b = map(int, sys.stdin.readline().split())
        present.append([_a, _b])

    present.sort(key=lambda x: x[1], reverse=True)
    present.sort(key=lambda x: x[0])

    dp = [(-1, -1) for i in range(n + 1)]

    dp[0] = (0, present[0][1])
    # position = 0

    # print(present)

    parents = [(-1, present[i][1]) for i in range(n)]
    m_max = 1

    for i in range(1, n):
        # 이분탐색 x LCS
        # print(dp, present[i], m_max)
        if dp[m_max - 1][1] >= present[i][1]:
            dp[m_max] = (i, present[i][1])
            parents[i] = dp[m_max - 1]
            # position += 1
            m_max += 1
            # print()
            continue

        start_position = 0
        end_position = m_max - 1
        mid_position = (start_position + end_position) // 2
        while start_position <= end_position:
            mid_position = (start_position + end_position) // 2
            # print(start_position, end_position, mid_position, dp[mid_position], present[i])
            if dp[mid_position][1] > present[i][1]:
                start_position = mid_position + 1
            elif dp[mid_position][1] < present[i][1]:
                end_position = mid_position - 1
            else:
                break

        # if dp[mid_position][1] == present[i][1]:
        #     position = mid_position + 1

        #     parents[i] = dp[position - 1] if position - 1 >= 0 else (-1, parents[i][1])
        #     dp[position] = (i, present[i][1])
        #     continue

        position = (start_position + end_position) // 2
        # print(i, present[i], dp[position - 1], position, start_position, end_position)
        if position < 0:
            position = 0

        while dp[position][1] >= present[i][1]:
            position += 1

        parents[i] = dp[position - 1] if position - 1 >= 0 else (-1, parents[i][1])
        dp[position] = (i, present[i][1])

    # print(dp)
    # print(parents)
    sys.stdout.write(str(m_max) + "\n")

    m_index = dp[m_max - 1][0]
    # for i in range(n - 1, -1 , -1):
    #     if cable[i][1] != dp[m_max - 1][1]:
    #         continue
    #     m_index = i
    #     break
    # print(m_index, dp[m_max - 1])

    check = [False for _ in range(n)]
    # for i in range(n):
    #     if not (dp[m_index][0] == cable[i][0] and dp[m_index][1] == cable[i][1]):
    #         continue

    #     # for j in range(m_max):
    #     check[i] = True
    #     m_index += 1
    # print(check, dp)
    # print(m_index, m_max, dp[m_max][0])
    while parents[m_index][0] != -1 and parents[m_index][0] != m_index:
        check[m_index] = True
        m_index = parents[m_index][0]
    check[m_index] = True

    # print(cable)
    # print(dp, m_max)
    # print(parents)
    # print(check)

    for i in range(n):
        if not check[i]:
            continue

        sys.stdout.write(str(present[i][0]) + " " + str(present[i][1]) + "\n")
