# 백준 1938 / 통나무 옮기기
# 가로와 세로의 길이가 같은 평지에서 벌목을 한다.
# 그 지형은 0과 1로 나타나 있다.
# 1은 아직 자르지 않은 나무를 나타내고 0은 아무 것도 없음을 나타낸다.
# BBB를 EEE에 옮기는 경로의 최소 길이는?

# 통나무 옮기기, 상하좌우 이동 가능.
# 90도 회전 가능 (주위에 나무 없을 때)

# 모르겠어서 답지 보는 중...ㅎㅎ
# https://rebas.kr/774
# ㄴ 답지 코드 (python)


"""
5
B0011
B0000
B0000
11000
EEE00

Answer : 9
"""


from collections import deque
from sys import stdin
input = stdin.readline


# 평지에서 벗어나는지 체크
def out(x, y):
    return x < 0 or x >= n or y < 0 or y >= n


# 중심점이 이동할 수 있는 공간인지 체크
def check(x, y):
    if out(x, y) or a[x][y] == '1':
        return False
    else:
        return True


# ?
def one(x, y, z, dx, dy):
    if not out(x+dx, y+dy) and a[x+dx][y+dy] != '1' and dist[x][y][z] == -1:
        q.append((x, y, z))
        dist[x][y][z] = dist[x-dx][y-dy][z]+1


# ?
def three(x, y, z, nx, ny, dx, dy):
    if not out(nx, ny) and dist[nx][ny][z] == -1:
        if a[nx][ny] != '1' and a[nx-dx][ny-dy] != '1' and a[nx+dx][ny+dy] != '1':
            q.append((nx, ny, z))
            dist[nx][ny][z] = dist[x][y][z]+1


# 회전시키기
def rotate(x, y, z):
    # 주변 8방향을 살피면서 나무가 존재하는지 체크.
    for dx, dy in (-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1, 1):
        nx, ny = x+dx, y+dy
        # 만약 나무가 존재하면 회전 불가. 함수 종료.
        if not check(nx, ny):
            return
    # 회전이 가능하고 첫 회전일 시 (중복해서 더해가면 안되니까)
    if dist[x][y][not z] == -1:
        q.append((x, y, not z))
        dist[x][y][not z] = dist[x][y][z]+1


# 너비 우선 탐색 활용
def bfs():
    while q:
        x, y, z = q.popleft()
        mx, my = 0, 0
        # 통나무가 가로 상태일 때
        if z:
            mx = 1
        # 통나무가 세로 상태일 때
        else:
            my = 1
        # 목적지 도달 시 거리 출력 후 종료
        if a[x][y] == 'E' and a[x-mx][y-my] == 'E' and a[x+mx][y+my] == 'E':
            print(dist[x][y][z])
            return
        # 목적지에 아직 도달하지 않은 경우
        # 이동 가능하면 거리 업데이트 후 해당 좌표 q에 넣어 짐
        # 통나무가 가로 상태일 때
        if z:
            one(x-1, y, z, -1, 0)
            one(x+1, y, z, 1, 0)
            three(x, y, z, x, y+1, 1, 0)
            three(x, y, z, x, y-1, 1, 0)
            rotate(x, y, z)
        # 통나무가 세로 상태일 때
        else:
            one(x, y-1, z, 0, -1)
            one(x, y+1, z, 0, 1)
            three(x, y, z, x+1, y, 0, 1)
            three(x, y, z, x-1, y, 0, 1)
            rotate(x, y, z)
    print(0)


# 평지 크기, 평지 상태 값 입력 받기
n = int(input())
a = [list(input().strip()) for _ in range(n)]
v = []
# 평지 상태 체크
for i in range(n):
    for j in range(n):
        # 통나무 위치
        if a[i][j] == 'B':
            v.append((i, j))
x, y = v[1]
_x, _y = v[0]
# 세로 상태면 _x == x, 가로 상태면 _x != x
# 즉, 통나무가 가로 상태면 z = True
z = (_x != x)
q = deque()
# 통나무 회전 상태에 따른 거리값 체크
dist = [[[-1, -1] for _ in range(n)] for _ in range(n)]
# 통나무 중심점 q에 넣기
q.append((x, y, z))
dist[x][y][z] = 0
# BBB => EEE : 경로의 최소 길이 구하기
bfs()

print("\n> dist 상태 : ")
for di in dist:
    for dj in di:
        print(dj, " ", end='\t')
    print()

