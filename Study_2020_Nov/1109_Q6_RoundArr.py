# 백준 16926 / 배열 돌리기 1
# 크기가 N X M인 배열을 R번 회전시킨 결과 구하기

# 2 ≤ N, M ≤ 300
# 1 ≤ R ≤ 1,000
# min(N, M) mod 2 = 0
# 1 ≤ Aij ≤ 108


"""
4 4 2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

Answer :
3 4 8 12
2 11 10 16
1 7 6 15
5 9 13 14
"""


import sys


# 배열의 세로길이(n), 가로길이(m)
# 회전 수(r)
n, m, r = map(int, sys.stdin.readline().rstrip().split())
# 배열 입력 받기
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

peel_n = min(n, m) // 2
rotation = [r] * peel_n
sero, garo = n, m
i = 0
# 껍질 단위로 회전 수 구하기
while i < peel_n:
    rotation[i] %= (sero + garo) * 2 - 4
    i += 1
    sero -= 2
    garo -= 2

print(rotation)


# 회전 함수
def rotate(target_peel, n, m):
    print(f'----- target_peel : {target_peel} -----')
    for _ in range(rotation[target_peel]):
        # 오른쪽으로 전진
        target_i = target_peel
        for j in range(target_peel, m - 2 * target_peel - 1):
            arr[target_i][j], arr[target_i][j+1] =\
                arr[target_i][j+1], arr[target_i][j]

        for i in range(n):
            print(*arr[i])
        print(f"ㄴ 오른쪽 이동 {m - 2 * target_peel - 1}\n")

        # 아래로 전진
        target_j = m - target_peel - 1
        for i in range(target_peel, n - 2 * target_peel - 1):
            arr[i][target_j], arr[i+1][target_j] =\
                arr[i+1][target_j], arr[i][target_j]

        for i in range(n):
            print(*arr[i])
        print("ㄴ 아래 이동\n")

        # 왼쪽으로 전진
        target_i = n - target_peel - 1
        for j in range(m - 2 * target_peel - 1, target_peel, -1):
            arr[target_i][j], arr[target_i][j - 1] = \
                arr[target_i][j - 1], arr[target_i][j]

        for i in range(n):
            print(*arr[i])
        print("ㄴ 왼쪽 이동\n")

        # 위로 전진
        target_j = target_peel
        for i in range(n - 2 * target_peel - 1, target_peel + 1, -1):
            arr[i][target_j], arr[i-1][target_j] =\
                arr[i-1][target_j], arr[i][target_j]

        for i in range(n):
            print(*arr[i])
        print("ㄴ 위로 이동\n")


# 껍질 단위로 회전 수행
for i in range(peel_n):
    rotate(i, n, m)

# 답 출력
for i in range(n):
    print(*arr[i])
