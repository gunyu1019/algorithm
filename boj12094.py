import sys
# import time


memory = [0 for _ in range(11)]


def more_deepcopy(_board: list[list[int]]) -> list[list[int]]:
    _new_board = []
    for __board in _board:
        _new_board.append(__board[:])
    return _new_board


# 1. 로직개선 (5개 반복문 => 2개 반복문)
def moving(_board: list[list[int]], _direction: int) -> list[list[int]]:
    _n = len(_board)
    if _direction == 0:  # LEFT
        for _i in range(_n):
            _new_board = []
            _last_x = -1
            for _j in range(_n):
                if _board[_i][_j] == 0:
                    continue

                # print(_new_board, _last_x, _i, _j, _board[_i][_j])
                if _board[_i][_last_x] == _board[_i][_j] and _last_x >= 0:
                    _new_board[-1] = _board[_i][_j] * 2
                    _last_x = -1
                    continue
                _new_board.append(_board[_i][_j])
                _last_x = _j

            for _j in range(_n):
                if len(_new_board) > _j:
                    _board[_i][_j] = _new_board[_j]
                else:
                    _board[_i][_j] = 0

            # for _j in range(_n):
            #     if len(_new_board) > _j:
            #         _board[_i][_j] = _new_board[_j]
            #         continue
            #     _board[_i][_j] = 0

            # for _j in range(_n - 1):
            #     if _board[_i][_j] == _board[_i][_j + 1] and _board[_i][_j] > 0:
            #         _board[_i][_j] += _board[_i][_j + 1]
            #         _board[_i][_j + 1] = 0

            # _new_board = []
            # for _j in range(_n):
            #     if _board[_i][_j] > 0:
            #         _new_board.append(_board[_i][_j])

            # for _j in range(_n):
            #     if len(_new_board) > _j:
            #         _board[_i][_j] = _new_board[_j]
            #         continue
            #     _board[_i][_j] = 0
    elif _direction == 1:  # TOP
        for _i in range(_n):
            _new_board = []
            _last_y = -1
            for _j in range(_n):
                if _board[_j][_i] == 0:
                    continue

                # print(_new_board, _last_y, _i, _j, _board[_i][_j])
                if _last_y >= 0 and _board[_j][_i] == _board[_last_y][_i]:
                    _new_board[-1] = _board[_j][_i] * 2
                    _last_y = -1
                    continue
                _new_board.append(_board[_j][_i])
                _last_y = _j

            for _j in range(_n):
                if len(_new_board) > _j:
                    _board[_j][_i] = _new_board[_j]
                else:
                    _board[_j][_i] = 0
            # _new_board = []
            # for _j in range(_n):
            #     if _board[_j][_i] > 0:
            #         _new_board.append(_board[_j][_i])

            # for _j in range(_n):
            #     if len(_new_board) > _j:
            #         _board[_j][_i] = _new_board[_j]
            #         continue
            #     _board[_j][_i] = 0

            # for _j in range(_n - 1):
            #     if _board[_j][_i] == _board[_j + 1][_i] and _board[_j][_i] > 0:
            #         _board[_j][_i] += _board[_j + 1][_i]
            #         _board[_j + 1][_i] = 0

            # _new_board = []
            # for _j in range(_n):
            #     if _board[_j][_i] > 0:
            #         _new_board.append(_board[_j][_i])

            # for _j in range(_n):
            #     if len(_new_board) > _j:
            #         _board[_j][_i] = _new_board[_j]
            #         continue
            #     _board[_j][_i] = 0
    elif _direction == 2:  # RIGHT
        for _i in range(_n):
            _new_board = []
            _last_x = -1
            for _j in range(_n - 1, -1, -1):
                if _board[_i][_j] == 0:
                    continue

                # print(_new_board, _last_x, _i, _j, _board[_i][_j])
                if _last_x >= 0 and _board[_i][_last_x] == _board[_i][_j]:
                    _new_board[-1] = _board[_i][_j] * 2
                    _last_x = -1
                    continue
                _new_board.append(_board[_i][_j])
                _last_x = _j

            # print(_new_board)
            for _j in range(_n):
                if len(_new_board) > _j:
                    _board[_i][_n - _j - 1] = _new_board[_j]
                else:
                    _board[_i][_n - _j - 1] = 0
            # _new_board = []
            # for _j in range(_n):
            #     if _board[_i][_n - _j - 1] > 0:
            #         _new_board.append(_board[_i][_n - _j - 1])

            # for _j in range(_n):
            #     if len(_new_board) > _j:
            #         _board[_i][_n - _j - 1] = _new_board[_j]
            #         continue
            #     _board[_i][_n - _j - 1] = 0

            # for _j in range(_n - 1):
            #     if _board[_i][_n - _j - 1] == _board[_i][_n - _j - 2] and _board[_i][_n - _j - 1] > 0:
            #         _board[_i][_n - _j - 1] += _board[_i][_n - _j - 2]
            #         _board[_i][_n - _j - 2] = 0

            # _new_board = []
            # for _j in range(_n):
            #     if _board[_i][_n - _j - 1] > 0:
            #         _new_board.append(_board[_i][_n - _j - 1])

            # for _j in range(_n):
            #     if len(_new_board) > _j:
            #         _board[_i][_n - _j - 1] = _new_board[_j]
            #         continue
            #     _board[_i][_n - _j - 1] = 0
    elif _direction == 3:  # DOWN
        for _i in range(_n):
            _new_board = []
            _last_y = -1
            for _j in range(_n - 1, -1, -1):
                if _board[_j][_i] == 0:
                    continue

                # print(_new_board, _last_y, _i, _j, _board[_j][_i])
                if _last_y >= 0 and _board[_last_y][_i] == _board[_j][_i]:
                    _new_board[-1] = _board[_j][_i] * 2
                    _last_y = -1
                    continue
                _new_board.append(_board[_j][_i])
                _last_y = _j

            # print(_new_board)
            for _j in range(_n):
                if len(_new_board) > _j:
                    _board[_n - _j - 1][_i] = _new_board[_j]
                else:
                    _board[_n - _j - 1][_i] = 0
            # _new_board = []
            # for _j in range(_n):
            #     if _board[_n - _j - 1][_i] > 0:
            #         _new_board.append(_board[_n - _j - 1][_i])

            # for _j in range(_n):
            #     if len(_new_board) > _j:
            #         _board[_n - _j - 1][_i] = _new_board[_j]
            #         continue
            #     _board[_n - _j - 1][_i] = 0

            # for _j in range(_n - 1):
            #     if _board[_n - _j - 1][_i] == _board[_n - _j - 2][_i] and _board[_n - _j - 1][_i] > 0:
            #         _board[_n - _j - 1][_i] += _board[_n - _j - 2][_i]
            #         _board[_n - _j - 2][_i] = 0

            # # print(_board)
            # _new_board = []
            # for _j in range(_n):
            #     if _board[_n - _j - 1][_i] > 0:
            #         _new_board.append(_board[_n - _j - 1][_i])

            # for _j in range(_n):
            #     if len(_new_board) > _j:
            #         _board[_n - _j - 1][_i] = _new_board[_j]
            #         continue
            #     _board[_n - _j - 1][_i] = 0
    return  _board


def simulation(_board: list[list[int]], _n: int) -> int:
    max_v = 0
    for _i in _board:
        max_v = max(max_v, max(_i))

    # 2. 마지막은 무조건 대충 연산해버리기 (판의 상세값을 알 필요가 없음.)
    if _n == 9:
        temp = max_v
        for _i in range(_n):
            memory[_n - _i] = max(memory[_n - _i], temp)
            if temp > 0:
                temp //= 2

        last_y = [-1 for _ in range(len(_board))]
        # print(_board)
        for _i in range(len(_board)):
            last_x = -1
            for _j in range(len(_board)):
                if _board[_i][_j] == 0:
                    continue

                # print(_board, max_v, last_y, last_x)
                if (
                    _board[_i][_j] >= max_v
                    and ((_board[_i][_j] == _board[_i][last_x] and last_x >= 0)
                    or  (_board[_i][_j] == _board[last_y[_j]][_j] and last_y[_j] >= 0)
                )):
                    memory[10] = max_v = _board[_i][_j] * 2
                last_x = _j
                last_y[_j] = _i

        return max_v
    
    # 3. 백트래킹 (depth에서 보다 더 깊게 판 경우가 없으면 제외시켜버리기)
    if memory[_n] > max_v:
        return max_v
    
    # 4. 소스코드 개선 (5번 요소로 결괏값이 없는 경우가 발생 = 에러! 에러!)
    result = [max_v]

    for _i in range(4):
        new_board = moving(more_deepcopy(_board), _i)
        
        # 5. 판의 변화가 없으면 굳이 시뮬레이션을 할 필요도 없다. 
        #    (판을 압축해서 연산해보려고 했으나 0.5초 연산이 필요해짐)
        if new_board == _board:
            continue

        result.append(
            simulation(new_board, _n + 1)
        )
    return max(result)


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    board = [list() for _ in range(n)]
    for i in range(n):
        board[i] = list(map(int, sys.stdin.readline().split()))

    # print(moving(more_deepcopy(board), 0))
    # print(moving(more_deepcopy(board), 1))
    # print(moving(more_deepcopy(board), 2))
    # print(moving(more_deepcopy(board), 3))
    # time1 = time.time()
    print(simulation(board, 0))

    # time2 = time.time()
    # print(time2 - time1)
