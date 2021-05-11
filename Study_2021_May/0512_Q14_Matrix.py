# 프로그래머스 Level2 행렬 테두리 회전하기
# 행렬에는 1부터 rows x columns까지의 숫자가 한 줄씩 순서대로 적혀있다.
# 이 행렬에서 직사각형 모양의 범위를 여러 번 선택해,
# 테두리 부분에 있는 숫자들을 시계방향으로 회전시키려 한다.
# 회전에 의해 위치가 바뀐 숫자들 중 가장 작은 숫자들을 순서대로 배열에 담아 return 하라.

# rows, columns 는 2 이상 100 이하
# 행렬에는 가로 방향으로 숫자가 1부터 하나씩 증가하면서 적혀있다.
# queries 의 행의 개수(회전의 개수)는 1 이상 10,000 이하
# queries의 각 행은 4개의 정수 [x1, y1, x2, y2]
#   ㄴ 1 ≤ x1 < x2 ≤ rows, 1 ≤ y1 < y2 ≤ columns
#   ㄴ 모든 회전은 순서대로 이루어진다.

import pprint


def solution(rows, columns, queries):
    answer = []

    matrix = [[i+j*columns+1 for i in range(columns)] for j in range(rows)]
    pprint.pprint(matrix, indent=4, width=40)
    print("--------------------------------------")

    for q in queries:
        answer.append(rotate(matrix, q))
    pprint.pprint(matrix, indent=4, width=40)

    return answer


def rotate(matrix, query) -> int:
    y1, x1, y2, x2 = query
    y1, x1, y2, x2 = y1-1, x1-1, y2-1, x2-1
    # 회전에 의해 위치가 바뀐 숫자들 중 가장 작은 숫자
    minimum = matrix[y1][x1]
    # 꼭지점 값 임시 저장
    corner = []
    corner.append(matrix[y1][x2])
    corner.append(matrix[y2][x1])
    corner.append(matrix[y2][x2])
    for c in corner:
        minimum = min(minimum, c)
    # 위에 테두리
    for i in range(x2, x1, -1):
        matrix[y1][i] = matrix[y1][i-1]
        minimum = min(minimum, matrix[y1][i])
    # 오른쪽 테두리
    for j in range(y2, y1, -1):
        matrix[j][x2] = matrix[j-1][x2]
        minimum = min(minimum, matrix[j][x2])
    matrix[y1+1][x2] = corner[0]
    # 아래 테두리
    for i in range(x1, x2-1):
        matrix[y2][i] = matrix[y2][i+1]
        minimum = min(minimum, matrix[y2][i])
    matrix[y2][x2-1] = corner[2]
    # 왼쪽 테두리
    for j in range(y1, y2-1):
        matrix[j][x1] = matrix[j+1][x1]
        minimum = min(minimum, matrix[j][x1])
    matrix[y2-1][x1] = corner[1]

    return minimum


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))  # [8, 10, 25]
# print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))  # [1, 1, 5, 3]
# print(solution(100, 97, [[1, 1, 100, 97]]))  # [1]


# 다른 사람의 풀이
def solution_another(rows, columns, queries):
    matrix = [list(range(r * columns + 1, r * columns + columns + 1))
              for r in range(rows)]

    ans = []
    for x1, y1, x2, y2 in queries:
        arr = matrix[x1 - 1][y1-1:y2] + \
              [matrix[i][y2-1] for i in range(x1-1, x2)][1:-1] + \
              matrix[x2 - 1][y1-1:y2][::-1] + \
              [matrix[i][y1-1] for i in range(x1-1, x2)][::-1][1:-1]
        ans.append(min(arr))

        arr = [arr[-1]] + arr[:-1]
        a, b = arr[:y2-y1+1], arr[y2-y1+1: y2-y1 + x2-x1]
        c, d = arr[y2-y1+x2-x1:y2-y1+x2-x1+y2-y1+1], arr[y2-y1+x2-x1+y2-y1+1:]
        matrix[x1 - 1][y1-1:y2] = a
        matrix[x2 - 1][y1-1:y2] = c[::-1]

        matrix = list(map(list, zip(*matrix)))
        matrix[y2-1][x1:x2-1] = b
        matrix[y1-1][x1:x2-1] = d[::-1]
        matrix = list(map(list, zip(*matrix)))

    return ans

