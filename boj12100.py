import sys


def more_deepcopy(_board: list[list[int]]) -> list[list[int]]:
    _new_board = []
    for __board in _board:
        _new_board.append(__board[:])
    return _new_board


def moving(_board: list[list[int]], _direction: int) -> list[list[int]]:
    _n = len(_board)
    # P. S. 규칙성이 있기 때문에 소스코드 길이를 줄일 순 있어요. 귀찮을--뿐!
    if _direction == 0:  # LEFT
        for _i in range(_n):
            _new_board = []
            for _j in range(_n):
                if _board[_i][_j] > 0:
                    _new_board.append(_board[_i][_j])

            for _j in range(_n):
                if len(_new_board) > _j:
                    _board[_i][_j] = _new_board[_j]
                    continue
                _board[_i][_j] = 0

            for _j in range(_n - 1):
                if _board[_i][_j] == _board[_i][_j + 1] and _board[_i][_j] > 0:
                    _board[_i][_j] += _board[_i][_j + 1]
                    _board[_i][_j + 1] = 0

            _new_board = []
            for _j in range(_n):
                if _board[_i][_j] > 0:
                    _new_board.append(_board[_i][_j])

            for _j in range(_n):
                if len(_new_board) > _j:
                    _board[_i][_j] = _new_board[_j]
                    continue
                _board[_i][_j] = 0
    elif _direction == 1:  # TOP
        for _i in range(_n):
            _new_board = []
            for _j in range(_n):
                if _board[_j][_i] > 0:
                    _new_board.append(_board[_j][_i])

            for _j in range(_n):
                if len(_new_board) > _j:
                    _board[_j][_i] = _new_board[_j]
                    continue
                _board[_j][_i] = 0

            for _j in range(_n - 1):
                if _board[_j][_i] == _board[_j + 1][_i] and _board[_j][_i] > 0:
                    _board[_j][_i] += _board[_j + 1][_i]
                    _board[_j + 1][_i] = 0

            _new_board = []
            for _j in range(_n):
                if _board[_j][_i] > 0:
                    _new_board.append(_board[_j][_i])

            for _j in range(_n):
                if len(_new_board) > _j:
                    _board[_j][_i] = _new_board[_j]
                    continue
                _board[_j][_i] = 0
    elif _direction == 2:  # RIGHT
        for _i in range(_n):
            _new_board = []
            for _j in range(_n):
                if _board[_i][_n - _j - 1] > 0:
                    _new_board.append(_board[_i][_n - _j - 1])

            for _j in range(_n):
                if len(_new_board) > _j:
                    _board[_i][_n - _j - 1] = _new_board[_j]
                    continue
                _board[_i][_n - _j - 1] = 0

            for _j in range(_n - 1):
                if _board[_i][_n - _j - 1] == _board[_i][_n - _j - 2] and _board[_i][_n - _j - 1] > 0:
                    _board[_i][_n - _j - 1] += _board[_i][_n - _j - 2]
                    _board[_i][_n - _j - 2] = 0

            _new_board = []
            for _j in range(_n):
                if _board[_i][_n - _j - 1] > 0:
                    _new_board.append(_board[_i][_n - _j - 1])

            for _j in range(_n):
                if len(_new_board) > _j:
                    _board[_i][_n - _j - 1] = _new_board[_j]
                    continue
                _board[_i][_n - _j - 1] = 0
    elif _direction == 3:  # DOWN
        for _i in range(_n):
            _new_board = []
            for _j in range(_n):
                if _board[_n - _j - 1][_i] > 0:
                    _new_board.append(_board[_n - _j - 1][_i])

            for _j in range(_n):
                if len(_new_board) > _j:
                    _board[_n - _j - 1][_i] = _new_board[_j]
                    continue
                _board[_n - _j - 1][_i] = 0

            for _j in range(_n - 1):
                if _board[_n - _j - 1][_i] == _board[_n - _j - 2][_i] and _board[_n - _j - 1][_i] > 0:
                    _board[_n - _j - 1][_i] += _board[_n - _j - 2][_i]
                    _board[_n - _j - 2][_i] = 0

            # print(_board)
            _new_board = []
            for _j in range(_n):
                if _board[_n - _j - 1][_i] > 0:
                    _new_board.append(_board[_n - _j - 1][_i])

            for _j in range(_n):
                if len(_new_board) > _j:
                    _board[_n - _j - 1][_i] = _new_board[_j]
                    continue
                _board[_n - _j - 1][_i] = 0
    return  _board


def simulation(_board: list[list[int]], _n: int) -> int:
    # print(_n, _board)
    if _n == 5:
        max_v = 0
        for _i in _board:
            max_v = max(max_v, max(_i))
        return max_v

    result = []
    for _i in range(4):
        new_board = moving(more_deepcopy(_board), _i)
        result.append(
            simulation(new_board, _n + 1)
        )
    return max(result)


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    board = [list() for _ in range(n)]
    for i in range(n):
        board[i] = list(map(int, sys.stdin.readline().split()))

    # print(moving(board, 3))
    print(simulation(board, 0))
