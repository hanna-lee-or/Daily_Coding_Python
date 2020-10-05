#라인 코딩 테스트 4번


def solution(maze):
    answer = 0

    # 출발 위치
    charactor = [1, 1]
    mazeSize = len(maze[0])

    # 상 하 좌 우 + 대각선 방향 정의 (반시계 방향)
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, -1, -1, -1, 0, 1, 1, 1]

    # 시뮬레이션 시작
    count = 0
    turn_time = 0

    # 초기 벽 탐색
    if(maze[0][1] == 1):
        current_wall = [0, 1]
        direction = 2
    else:
        current_wall = [-1, 0]
        direction = 4

    while True:
        # 왼쪽에 벽이 있으면 해당 벽 좌표 반환
        # 해당 벽이 캐릭터 좌표 기준으로 반시계방향으로 타일 분석
        # 다른 벽 타일 발견 시 해당 벽 타일로 전환 후 부딪히기 직전
        # 좌표로 캐릭터 이동 (부딪히기 전까지 밟은 타일 카운트)
        # 좌표계 벗어난 부분은 벽으로 처리
        for i in range(8):
            direction += 1
            if(direction >= 8):
                direction = 0
            nx = current_wall[0] + dx[direction]
            ny = current_wall[1] + dy[direction]
            # 새로운 벽 발견 시
            if(nx < 0 or nx >= mazeSize or ny < 0 or ny >= mazeSize):
                current_wall = [nx, ny]
                break
            elif(maze[nx][ny] == 1):
                current_wall = [nx, ny]
                break
            # 아니면 캐릭터 이동
            else:
                charactor[0] = nx
                charactor[1] = ny
                count += 1
                print("이동 :", charactor)
                if (charactor[0] == mazeSize - 1 & charactor[1] == mazeSize - 1):
                    return count

        print("벽 발견 :", current_wall)
        temp_dirX = charactor[0] - current_wall[0]
        temp_dirY = charactor[1] - current_wall[1]
        # 새로운 방향 찾기
        for i in range(8):
            if(dx[i] == temp_dirX and dy[i] == temp_dirY):
                direction = i



print(solution(	[[0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0]]))


