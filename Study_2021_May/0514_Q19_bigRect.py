# 프로그래머스 Level2 가장 큰 정사각형 찾기
# 1와 0로 채워진 표(board)가 있습니다.
# 1로 이루어진 가장 큰 정사각형을 찾아 넓이를 return 하세요.

# 행(row), 열(column) 의 크기 : 1,000 이하
# 표(board)의 값은 1또는 0으로만 구성

import pprint
import math
from collections import defaultdict


# 나의 답안. 효율성 X.
def solution(board):
    answer = 0

    row = len(board)
    column = len(board[0])

    # 0 위치 기록
    zero_dict = defaultdict(list)
    for i, r in enumerate(board):
        for j, c in enumerate(r):
            if c == 0:
                zero_dict[i].append(j)
            else:
                answer += 1
    if answer == 0:
        return 0

    r = int(math.sqrt(answer))
    # 정사각형 범위를 좁혀가며 탐색
    while r > 1:
        for i in range(row-r+1):
            for j in range(column-r+1):
                # (i, j) ~ (i+r, j+r) 범위에 0이 없으면 ok
                print(f"({i}, {j}) 시작점 // {r}")
                flag = True
                for gab in range(r):
                    for zero_j in zero_dict[i+gab]:
                        if j <= zero_j < j+r:
                            flag = False
                            break
                    if not flag:
                        break
                if flag:
                    return r*r
        r -= 1

    return 1


# print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))  # 9
print(solution([[0, 0, 1, 1], [1, 1, 1, 1]]))  # 4


# 다른 사람의 풀이. DP 활용.
# 1 1 1
# 1 2 2
# 1 2 3  => 최대넓이 : 3
def solution_another(board):
    for row in board:  # 정답의 최소값이 0인지 1인지 먼저 판별
        if sum(row):
            answer = 1
            break
    else:
        return 0
    # 1행 1열부터 board 를 2x2 정사각형으로 탐색하면서 우측 아래 값 최신화
    for i in range(1, len(board)):  # 행
        for j in range(1, len(board[0])):  # 열
            if board[i-1][j-1] and board[i-1][j] and board[i][j-1] and board[i][j]:
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1
                answer = max(answer, board[i][j])
    return answer ** 2


def findLargestSquare1(board):
    answer = 1
    res = [[1 if x == 'O' else 0 for x in y] for y in board]
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == 'O':
                res[y][x] = min(res[y-1][x], res[y-1][x-1], res[y][x-1]) + 1
                if res[y][x] > answer:
                    answer = res[y][x]

    return answer ** 2


def findLargestSquare2(board):
    ss = {}
    answer = 0
    for y, line in enumerate(board):
        for x, v in enumerate(line):
            if v == 'X':
                continue
            ss[(x, y)] = s = min(
                ss.get((x-1, y), 0),
                ss.get((x, y-1), 0),
                ss.get((x-1, y-1), 0)
            ) + 1
            answer = max(answer, s ** 2)
    return answer

