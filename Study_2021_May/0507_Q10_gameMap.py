# 프로그래머스 Level2 게임 맵 최단거리
# 가장 빠르게 상대팀 진영에 도착하기. 최단 거리를 return. (불가능할 때는 -1)
# 캐릭터는 동, 서, 남, 북 방향으로 한 칸씩 이동할 수 있고,
# 게임 맵을 벗어난 길은 갈 수 없다.

# maps는 n x m 크기의 게임 맵의 상태가 들어있는 2차원 배열
# n과 m은 각각 1 이상 100 이하
# 0은 벽이 있는 자리, 1은 벽이 없는 자리
# 초기 캐릭터 위치는 게임 맵의 좌측 상단 (1, 1)
# 상대방 진영 위치은 게임 맵의 우측 하단 (n, m)

from pprint import pprint
from collections import deque


# 나의 답.
def solution(maps):

    # 맵 크기
    row = len(maps)
    column = len(maps[0])
    pprint(maps, indent=4, width=40)
    # 동, 남, 북, 서
    dir_x = [1, 0, 0, -1]
    dir_y = [0, -1, 1, 0]

    q = deque()
    q.append((0, 0))
    # BFS 탐색
    while q:
        x, y = q.popleft()
        d = maps[x][y]
        # 주변 탐색
        for i in range(4):
            nx = x + dir_x[i]
            ny = y + dir_y[i]
            if 0 <= nx < row and 0 <= ny < column:
                nd = maps[nx][ny]
                # 빠른 길은 다음 장소로 채택 & 거리 +1
                if nd != 0 and (nd == 1 or d + 1 < nd):
                    maps[nx][ny] = d + 1
                    q.append((nx, ny))
    pprint(maps, indent=4, width=40)

    # 풀 때는 while 문을 다 돌아야 한다고 생각해서
    # while 문 아래에 return 문을 작성했는데
    # 생각해보니 BFS 라서 먼저 도착하는 길이 지름길.
    # while 문 안에 도착지 확인 및 return 문 작성해도 OK.
    answer = maps[-1][-1]
    if answer == 1:
        return -1
    else:
        return answer


# print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1],
#                 [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))  # 11
print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1],
                [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))  # -1


# 다른 사람의 풀이. 먼저 도달하는 길이 빠른 길임.
# 따라서 while 문 돌면서 도착지 확인 시 바로 return 해도 OK.
def solution_another(maps):
    x_move = [1, 0, -1, 0]
    y_move = [0, 1, 0, -1]

    x_h, y_h = (len(maps[0]), len(maps))
    queue = deque([(0, 0, 1)])

    while queue:
        x, y, d = queue.popleft()

        for i in range(4):
            nx = x + x_move[i]
            ny = y + y_move[i]

            if -1 < nx < x_h and -1 < ny < y_h:
                if maps[ny][nx] == 1 or maps[ny][nx] > d + 1:
                    maps[ny][nx] = d + 1
                    if nx == x_h - 1 and ny == y_h - 1:
                        return d + 1

                    queue.append((nx, ny, d + 1))

    return -1
