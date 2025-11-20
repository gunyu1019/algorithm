import sys


# 이 문제를 풀며 사용한 알고리즘: LCS (이분탐색), 백트래킹, DP
if __name__ == '__main__':
    n = int(sys.stdin.readline())
    cable = []
    for _ in range(n):
        _s, _e = map(int, sys.stdin.readline().split())
        cable.append([_s, _e])

    cable.sort(key=lambda x: x[0])
    dp = [(-1, -1) for i in range(n + 1)]

    dp[0] = (0, cable[0][1])
    # position = 0

    # print(cable)

    parents = [(-1, cable[i][1]) for i in range(n)]
    m_max = 1

    for i in range(1, n):
        # 기존 방식은 O(N^2)의 시간 복잡도를 가지고 있기 때문에 시간초과를 초래할 수 있음.
        # = 따른 접근법이 필요함. 
        
        # for j in range(i):
        #     if cable[j][1] >= cable[i][1]:
        #         continue

        #     if dp[j] + 1 > dp[i]:
        #         dp[i] = dp[j] + 1
        #         parents[i] = j
        # print(i, dp, cable[i], m_max, end=' ')
        
        # 이분탐색 x LCS
        if dp[m_max - 1][1] < cable[i][1]:
            dp[m_max] = (i, cable[i][1])
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
            if dp[mid_position][1] > cable[i][1]:
                end_position = mid_position - 1
            elif dp[mid_position][1] < cable[i][1]:
                start_position = mid_position + 1
            else:
                break
        position = (start_position + end_position) // 2 + 1
        # print(i, cable[i], dp[position - 1], position, start_position, end_position)
        if position < 0:
            position = 0

        parents[i] = dp[position - 1] if position - 1 >= 0 else (-1, cable[i][1])
        dp[position] = (i, cable[i][1])

    sys.stdout.write(str(n - m_max) + "\n")

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
        if check[i]:
            continue

        sys.stdout.write(str(cable[i][0]) + "\n")
