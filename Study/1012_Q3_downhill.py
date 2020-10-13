# 백준 1520 / 내리막 길 (다이나믹)
# 각 지점의 높이가 적혀있는 지도.
# 상하좌우로 이동가능.
# 내리막길로 왼쪽 위 칸에서
# 오른쪽 아래 칸으로 도달하는 경우의 수

import sys
from sys import setrecursionlimit
setrecursionlimit(10**9)

n, m = map(int, sys.stdin.readline().rstrip().split())
info = []
sheet = [[-1] * m for _ in range(n)]
sheet[0][0] = 0
for i in range(n):
    info.append(list(map(int, sys.stdin.readline().rstrip().split())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def find_road(target):
    x, y = target
    if x == n - 1 and y == m - 1:
        return 1
    count = 0
    for k in range(4):
        next_x = x + dx[k]
        next_y = y + dy[k]
        if 0 <= next_x < n and 0 <= next_y < m:
            # 내리막길에 해당하는 경우
            if info[next_x][next_y] < info[x][y]:
                # 미완
                count += find_road([next_x, next_y])
    return count


print(find_road([0, 0]))
