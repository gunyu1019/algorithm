import collections
import sys


if __name__ == "__main__":
    # 귀차니즘 이슈
    cl = list(range(ord('A'), ord('Z') + 1)) + list(range(ord('a'), ord('z') + 1))
    
    # 파이프가 지날 수 있는 "최대" 유량
    capacity = {chr(w): dict() for w in cl}
    # 실제 흘러간 유량
    flow = {chr(w): dict() for w in cl}

    n = int(sys.stdin.readline())
    for _ in range(n):
        _s, _e, _l = sys.stdin.readline().split()

        if _e not in capacity[_s].keys():
            capacity[_s][_e] = 0
        if _e not in flow[_s].keys():
            flow[_s][_e] = 0
        
        # Duplicated Way (중복되는 경로) 가능.
        capacity[_e][_s] = capacity[_s][_e] = capacity[_s][_e] + int(_l) 
        flow[_e][_s] = flow[_s][_e] = 0

    total_amount = 0

    while True:
        q = collections.deque()
        q.append(("A", 0x7fffffff))

        parents = {chr(w): "" for w in cl}
        parents["A"] = "A"

        amount = 0
        # A to Z 경로 탐색 + 이동 가능한 유량 계산
        while len(q) > 0:
            p, l = q.popleft()

            # print(p, "->", l, flow[p], amount, parents[p])

            if p == "Z":
                amount = l
                break

            for np in capacity[p].keys():
                if parents[np] != "" or capacity[p][np] - flow[p][np] <= 0:
                    continue

                parents[np] = p
                q.append((np, min(l, capacity[p][np] - flow[p][np])))

        # No more way.
        if parents["Z"] == "":
            break

        # Z to A 유량 계산 반영
        p = "Z"
        while p != "A":
            flow[parents[p]][p] += amount
            # 유량 원칙에 따라 역방향에서 오는 유량을 고려함.
            flow[p][parents[p]] -= amount
            p = parents[p]

        total_amount += amount
        # ㅁㄴㅇㄹ. 시간 단축하고 싶어서 유량 계산과 경로 탐색을 동시에 해보았는데 변수 사항이 너무 많음.

    print(total_amount)
