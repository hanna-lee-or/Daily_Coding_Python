# 백준 1520 / 내리막 길 (다이나믹 DP)
# 각 지점의 높이가 적혀있는 지도.
# 상하좌우로 이동가능.
# 내리막길로 왼쪽 위 칸에서
# 오른쪽 아래 칸으로 도달하는 경우의 수

"""
4 5
50 45 37 32 30
35 50 40 20 25
30 28 25 17 28
27 24 22 15 10
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m = map(int, input().rstrip().split())
info = []
sheet = [[-1] * m for _ in range(n)]
sheet[0][0] = 0
for i in range(n):
    info.append(list(map(int, input().rstrip().split())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def find_road(x, y):
    # 도착지에 도달하면 경우의 수 + 1
    # 이전 지점으로 돌아가며 경우의 수 카운트해 감.
    if x == n - 1 and y == m - 1:
        return 1
    count = 0
    for k in range(4):
        next_x = x + dx[k]
        next_y = y + dy[k]
        # 주변에 내리막길이 없으면 아무것도 하지 않고 0 리턴
        if 0 <= next_x < n and 0 <= next_y < m:
            # 내리막길에 해당하는 경우
            if info[next_x][next_y] < info[x][y]:
                if sheet[next_x][next_y] >= 0:
                    count += sheet[next_x][next_y]
                else:
                    count += find_road(next_x, next_y)
    sheet[x][y] = count
    print("x :", x, "/ y :", y)
    for k in sheet:
        print(k)
    print()
    return count


print(find_road(0, 0))
print("------ Sheet ------")
for s in sheet:
    print(s)
