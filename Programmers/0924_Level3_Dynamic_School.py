# 프로그래머스 동적계획법(Dynamic) Level 3 등굣길
# 최단 경로 개수.
# Hanna 2020/09/24

# 왼쪽에서 오는 경우의 수 + 위쪽에서 오는 경우의 수가
# 현재 좌표의 총 경우의 수라는 것이 포인트!


# 다른 사람의 답
def solution_another(m, n, puddles):
    # 딕셔너리로 경우의 수 저장
    info = dict([((2, 1), 1), ((1, 2), 1)])
    # 장애물 있는 곳은 경우의 수 0으로
    for puddle in puddles:
        info[tuple(puddle)] = 0

    def func(m, n):
        if m < 1 or n < 1:
            return 0
        if (m, n) in info:
            return info[(m, n)]
        return info.setdefault((m, n), func(m - 1, n) + func(m, n - 1))

    return func(m, n) % 100000000


# 나의 답
def solution(m, n, puddles):

    # 지도 정보 입력
    ground = [[0] * (m+1) for i in range(n+1)]
    # 장애물 좌표 값이 거꾸로 들어온다는 점 유의!
    # for a, b in puddles:
    #     grid[b][a] = -1
    ground[1][1] = 1

    # 경우의 수 갱신
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            # if ground[i][j] == -1:
            if [j, i] in puddles:
                # 장애물이 있는 경우, 0으로 리셋
                ground[i][j] = 0
            else:
                # 왼쪽에서 오는 경우의 수 + 위쪽에서 오는 경우의 수
                ground[i][j] = ground[i-1][j] + ground[i][j-1]
                
    # 지도 상태
    for g in range(len(ground)):
        print(ground[g])

    return ground[n][m]


print('\nanswer :', solution(4, 3, [[2, 2], [1, 3]]))
