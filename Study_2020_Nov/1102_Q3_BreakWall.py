# 백준 2206 / 벽 부수고 이동하기
# 0은 이동할 수 있는 곳, 1은 이동할 수 없는 벽
# 왼쪽 위 (1, 1)에서 오른쪽 아래 (N, M)까지 이동하고자 함
# 최단 경로 길이는?
# 단, 벽 하나 부수기 가능
# 불가능할 때는 -1 출력

# 정답지 분석. BFS, DFS 이용하는 문제.

"""
6 4
0100
1110
1000
0000
0111
0000

Answer : 15
"""


import sys
from collections import deque


# 이동영역 세로길이(n), 가로길이(m)
n, m = map(int, sys.stdin.readline().rstrip().split())
# 이동 방향 (상, 하, 좌, 우)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 맵 정보
info = []
# 벽을 부수지 않았을 때의 경로 길이
dp = [[0] * m for _ in range(n)]
# 벽을 부쉈을 때의 경로 길이
dp_break = [[0] * m for _ in range(n)]

# 맵 정보 입력받기
for _ in range(n):
    row_info = list(map(int, sys.stdin.readline().rstrip()))
    info.append(row_info)
dp[0][0] = info[0][0]

# 가장 작은 경우 (백준 100% 지점)
if n == 1 and m == 1:
    print(max(n, m))
else:

    # DFS or BFS 경로 찾기
    # 시작 칸 큐에 넣기
    q = deque()
    q.append([[0, 0], False])

    # 시작 칸도 포함이므로 1부터 시작
    dp[0][0] = 1

    while q:
        pos, is_break = q.popleft()
        x, y = pos

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 체크
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            # 벽인 경우
            # is_break == False (벽을 부수지 않았고)
            # dp_break[nx][ny] == 0
            # (벽을 부순 상태로 다음 칸에 아직 방문하지 않은 경우)
            if info[nx][ny] == 1 and not is_break \
                and dp_break[nx][ny] == 0:
                q.append([[nx, ny], True])
                dp_break[nx][ny] = dp[x][y] + 1
            # 길인 경우
            # 이동할 칸에 방문하지 않았으면 방문
            elif info[nx][ny] == 0:
                if is_break and dp_break[nx][ny] == 0:
                    q.append([[nx, ny], True])
                    dp_break[nx][ny] = dp_break[x][y] + 1
                elif not is_break and dp[nx][ny] == 0:
                    q.append([[nx, ny], False])
                    dp[nx][ny] = dp[x][y] + 1

    # DP 테이블 상태 확인하기
    print("----- DP 테이블 -----")
    for d in dp:
        print(d)
    print("\n----- DP_BREAK 테이블 -----")
    for b in dp_break:
        print(b)

    # 마지막 칸의 최솟값 찾기
    # 정답 출력 (최단 거리)
    mini = dp[n-1][m-1]
    temp = dp_break[n-1][m-1]
    if mini != 0:
        if temp != 0 and mini > temp:
            mini = temp
    else:
        if temp != 0:
            mini = temp

    if mini == 0:
        print("-1")
    else:
        print(mini)

