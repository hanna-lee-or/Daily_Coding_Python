# 프로그래머스 Level3 합승 택시 요금
# A, B 두 사람이 s에서 출발해서 각각의 도착 지점까지 택시를 타고 간다고 가정할 때,
# 최저 예상 택시요금을 계산해서 return 하라.
# 합승은 하지 않아도 된다. A, B 는 S 에서 출발한다.

# [제한 조건]
# n은 3 이상 200 이하인 자연수.
# A, B 도착점은 서로 다름.
# fares 배열의 크기는 2 이상 n x (n-1) / 2 이하
# fares 원소는 [c, d, f] 형태. f 는 택시요금.
# 경로가 존재하는 경우만 입력으로 주어진다.

from math import inf
from collections import defaultdict
import heapq


# 나의 답.
def solution(n, s, a, b, fares):

    # 이동 최소비용을 저장할 2차원 배열
    cost = [[inf] * n for _ in range(n)]
    # 정보 저장
    for c, d, f in fares:
        cost[c - 1][d - 1] = f
        cost[d - 1][c - 1] = f

    # 플로이드 와샬 알고리즘 적용
    for k in range(n):
        cost[k][k] = 0
        for i in range(n):
            for j in range(n):
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

    # [1] A, B 로 이동해본다.
    answer = inf
    for i in range(n):
        f = cost[s-1][i] + cost[i][a-1] + cost[i][b-1]
        answer = min(answer, f)

    return answer


# 82
print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2],
                            [3, 1, 41], [5, 1, 24], [4, 6, 50],
                            [2, 4, 66], [2, 3, 22], [1, 6, 25]]))


# 다익스트라 사용
def solution_another(n, s, a, b, fares):
    dic = defaultdict(list)
    for st, ed, co in fares:
        dic[st].append((co, ed))
        dic[ed].append((co, st))
    ans = []
    for i in range(1, n+1):
        Q = [(0, i)]
        visited = [True] * (n+1)
        dp = [float('inf')] * (n+1)
        dp[i] = 0
        while Q:
            co, des = heapq.heappop(Q)
            if visited[des]:
                visited[des] = False
                for cost, destination in dic[des]:
                    dp[destination] = min(cost + dp[des], dp[destination])
                    heapq.heappush(Q, (dp[destination], destination))
        ans.append(dp[a] + dp[b] + dp[s])

    return min(ans)

