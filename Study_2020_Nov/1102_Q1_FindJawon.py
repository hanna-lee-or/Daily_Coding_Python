# 백준 14430 / 자원 캐기
# 인공지능 자원 캐기 로봇 WOOK
# 왼쪽 위 (1, 1)에서 오른쪽 아래 (N, M)까지 탐색
# 탐색 시 오른쪽 or 아래쪽으로 한 칸씩 이동 가능
# WOOK가 탐색할 수 있는 자원의 최대 숫자는?

"""
5 4
0 1 0 0
0 0 1 0
1 1 0 0
1 0 1 0
1 1 0 0

Answer : 4
"""


import sys


# 탐사영역 세로길이(n), 가로길이(m)
n, m = map(int, sys.stdin.readline().rstrip().split())

info = []
info.append([0 for _ in range(m+1)])
dp = [[0] * (m+1) for _ in range(n+1)]
# 탐사영역 정보 입력받기
for _ in range(n):
    row_info = list(map(int, sys.stdin.readline().rstrip().split()))
    info.append([0] + row_info)
dp[1][1] = info[1][1]

# 카운팅
for x in range(1, n+1):
    for y in range(1, m+1):
        dp[x][y] = max(dp[x][y-1], dp[x-1][y]) + info[x][y]


for d in dp:
    print(d)
print(dp[n][m])




