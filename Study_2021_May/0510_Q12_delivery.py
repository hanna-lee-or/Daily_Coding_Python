# 프로그래머스 Level3 배달
# N개의 마을로 이루어진 나라. 마을 간 도로. (이동 시간 상이)
# 현재 1번 마을에 있는 음식점에서 각 마을로 음식 배달을 하려고 한다.
# N개의 마을 중에서 K 시간 이하로 배달이 가능한 마을에서만 주문받을 예정.

# 마을의 개수 N, 각 마을을 연결하는 도로의 정보 road,
# 음식 배달이 가능한 시간 K가 매개변수로 주어질 때,
# 음식 주문을 받을 수 있는 마을의 개수를 return

# N은 1 이상 50 이하.
# road의 길이(도로 정보의 개수)는 1 이상 2,000 이하.
# road는 길이가 3인 배열이며, 순서대로 (a, b, c)
#   ㄴ c는 a, b 마을 연결 도로를 건너는 시간. (1 ≤ c ≤ 10,000)
#   ㄴ 두 마을 a, b를 연결하는 도로는 여러 개가 있을 수 있습니다.
# K는 음식 배달이 가능한 시간을 나타내며, 1 이상 500,000 이하.
# 임의의 두 마을간에 항상 이동 가능한 경로가 존재.
# 1번 마을에 있는 음식점이 K 이하의 시간에 배달이 가능한 마을의 개수는?

import heapq
import sys
sys.setrecursionlimit(10**6)


def solution(N, road, K):

    if N < 2:
        return 1

    inf = 9999999
    graph = [[inf for _ in range(N+1)] for _ in range(N+1)]

    for a, b, c in road:
        graph[a][b] = min(graph[a][b], c)
        graph[b][a] = min(graph[b][a], c)

    distance = [inf for _ in range(N+1)]
    q = []
    distance[1] = 0
    heapq.heappush(q, (distance[1], 1))  # 1번 도시를 기준으로 각 마을까지의 거리 구하기

    while q:
        d, n = heapq.heappop(q)
        print(n)

        if distance[n] < d:
            continue

        for i in range(1, N+1):
            # 연결되어 있고
            if graph[n][i] != inf:
                dis = d + graph[n][i]
                # 더 짧은 거리라면
                if dis < distance[i]:
                    distance[i] = dis
                    heapq.heappush(q, (dis, i))

    count = 0
    for d in distance:
        if d <= K:
            count += 1
    print("\n", distance)

    return count


print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2],
                   [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))  # 4
# print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2],
#                   [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1], 4))  # 4

