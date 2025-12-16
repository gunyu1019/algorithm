import sys


if __name__ == '__main__':
    while True:
        n, m = map(int, sys.stdin.readline().strip().split())
        if n == m == 0:
            break

        correct_directory = [dict() for _ in range(100)]  # max-depth: 100 (max-depth 50으로 잡아도 적당할지도?)
        for _ in range(n):
            path = sys.stdin.readline().strip().split("/")
            if len(path) == 2:
                correct_directory[0][path[1]] = []

            for depth, _path in enumerate(path[1:-1]):
                if correct_directory[depth].get(_path) is None:
                    correct_directory[depth][_path] = []
                correct_directory[depth][_path].append(path[depth + 2])

        def parse_and_inspect_path(inspect_path: list[str]) -> list[str] | None:
            is_ended_with_slash = inspect_path[-1] == ''
            parsed_inspect_path = []

            for _i, token in enumerate(inspect_path):
                if token == '':
                    continue

                _depth = len(parsed_inspect_path)
                prev_token = None
                if _depth > 0:
                    prev_token = parsed_inspect_path[-1]

                if token == '.':
                    continue
                elif token == '..':
                    if len(parsed_inspect_path) <= 0:
                        return None  # Non-Root (Root를 벗어남)
                    parsed_inspect_path.pop()
                    continue

                if prev_token is None:  # dir: root
                    # 폴더 or 파일 유무를 확인함.
                    if correct_directory[_depth].get(token) is None:
                        return None

                    # 파일 존재를 검사함. 다만 "/" 같이 정의된 경우 파일이 아니라 폴더라서 유형 오류 유발 가능성 있음
                    if len(correct_directory[_depth][token]) == 0 and is_ended_with_slash:
                        return None
                else:
                    # 폴더 존재를 검사함.
                    if token not in correct_directory[_depth - 1][prev_token]:
                        return None

                    # 마지막 인덱스가 아니라면 모든 토큰은 폴더로 존재해야 함.
                    if (
                        _i != len(inspect_path) - 1
                        and correct_directory[_depth].get(token) is None
                    ):
                        return None
                parsed_inspect_path.append(token)

            if len(parsed_inspect_path) == 0:
                # Case: '/' 또는 '/index.html' 같은 케이스인 경우 (맨 아래 케이스와 비슷함)
                if "index.html" in correct_directory[0].keys() and len(correct_directory[0]["index.html"]) == 0:
                    return ["index.html"]
                return None
            elif len(parsed_inspect_path) == 1:
                # Case: 아래의 케이스를 커버해줌. /A.hwp 와 같은 파일이 존재하는 경우
                file_name = parsed_inspect_path[0]
                if file_name in correct_directory[0].keys() and len(correct_directory[0][file_name]) == 0:
                    return parsed_inspect_path

            _depth = len(parsed_inspect_path)

            # Case: /A/B.hwp 와 같이 파일이 정의되어 있는 경우, 문제는 /A.hwp 유형은 커버해주지 못함.
            if (
                    len(parsed_inspect_path) >= 2
                    and parsed_inspect_path[-1] in correct_directory[_depth - 2][parsed_inspect_path[-2]]
                    and parsed_inspect_path[-1] not in correct_directory[_depth - 1].keys()
            ):
                if is_ended_with_slash:
                    return None
                return parsed_inspect_path

            # Case: /A/B/ 형태의 directory만 정의한 경우, "index.html"를 포함해서 추가 검사를 요구한다.
            if (
                "index.html" in correct_directory[_depth - 1].get(parsed_inspect_path[-1], list())
            ):
                parsed_inspect_path.append("index.html")
                return parsed_inspect_path

            return None

        for _ in range(m):
            inspect_path1 = sys.stdin.readline().strip().split("/")[1:]
            inspect_path2 = sys.stdin.readline().strip().split("/")[1:]

            parsed_inspect_path1 = parse_and_inspect_path(inspect_path1[:])
            parsed_inspect_path2 = parse_and_inspect_path(inspect_path2[:])

            if parsed_inspect_path1 is None or parsed_inspect_path2 is None:
                sys.stdout.write("not found\n")
            elif parsed_inspect_path1 == parsed_inspect_path2:
                sys.stdout.write("yes\n")
            else:
                sys.stdout.write("no\n")
