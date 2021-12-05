# 프로그래머스 Level2 빛의 경로 사이클
# 각 칸마다 S, L, R 이 써져 있는 격자가 있다.
# 이 격자에서 빛을 쏘았을 때 만들어지는 빛의 경로 사이클의 모든 길이들을 구하라.

# "S" : 직진
# "L" : 좌회전
# "R" : 우회전
# 빛이 격자 끝을 넘어갈 경우, 반대쪽 끝으로 다시 돌아온다.
# 격자 내에서 빛이 이동할 수 있는 경로 사이클이
# 몇 개 있고, 각 사이클의 길이가 얼마인지 알고 싶다.

# 격자는 직사각형 형태
# 1 <= grid 의 길이 <= 500
# 1 <= grid 의 각 문자열 길이 <= 500
# gird 모든 문자열의 길이는 서로 같으며 'L', 'R', 'S' 로만 이루어져있다.


# 나의 답안.
def solution(grid):
    answer = []

    # 격자의 가로 n, 세로 m
    n = len(grid)
    m = len(grid[0])
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    # 사이클은 최대 4개? => 아닐 수도 있음
    # 빛이 가지 않은 경로를 찾아내서 사이클 돌려야 함
    # 경로 리스트도 있어야 하나?
    path = [[[False] * 4 for _ in range(m)] for _ in range(n)]

    # 1. 빛을 쏜다
    # 2. 경로 체크하며 빛을 이동시킨다
    # 3. 쏜 위치로 되돌아오면 사이클 기록
    # 4. path 에 False 인 곳이 있는지 체크한다.
    # 5. 있으면 1로 돌아간다. 없으면 answer 을 반환한다.

    # d 는 방향. d => [상 0, 좌 1, 하 2, 우 3]
    # [sx, sy] 좌표에서 d 방향으로 빛을 쏜다.
    def shoot_light(sx, sy, sd):
        x, y, d = sx, sy, sd
        path[x][y][d] = True
        count = 0
        # 빛 이동
        while True:
            # 빛의 방향에 따라 다음 칸으로 이동
            x = (x + dx[d]) % n
            y = (y + dy[d]) % m
            count += 1

            # 칸 종류에 따라 빛의 방향 세팅
            grid_data = grid[x][y]
            if grid_data == 'L':
                d = (d+1) % 4
            elif grid_data == 'R':
                d = (d-1) % 4

            # 이미 거쳤던 경로라면
            if path[x][y][d]:
                # 사이클이 완성된 경우
                if (x, y, d) == (sx, sy, sd):
                    return count
                # 사이클이 아닌 경우 (= 부분 사이클)
                else:
                    return 0
            else:
                # 새로운 경로라면 방문 처리
                path[x][y][d] = True

    # 빛을 경로 별로 쏘아 사이클을 체크
    for start_x in range(n):
        for start_y in range(m):
            for direction in range(4):
                if not path[start_x][start_y][direction]:
                    print("---------------------------------------")
                    print([len(answer)], "번째 shoot_light")
                    print("start 지점", [start_x, start_y])
                    print("빛의 방향", [direction])
                    print("ㄴ d => [상 0, 좌 1, 하 2, 우 3]")
                    cycle_len = shoot_light(start_x, start_y, direction)
                    if cycle_len != 0:
                        answer.append(cycle_len)

    answer.sort()
    return answer


# [16]
print("\n>> print(solution([\"SL\", \"LR\"])) <<")
print(solution(["SL", "LR"]))
# [1, 1, 1, 1]
print("\n>> print(solution([\"S\"])) <<")
print(solution(["S"]))
# [4, 4]
print("\n>> print(solution([\"R\", \"R\"])) <<")
print(solution(["R", "R"]))









