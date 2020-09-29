# 프로그래머스 Graph Level 3 가장 먼 노드
# 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지
# Hanna 2020/09/29

# BFS 선입선출! 기억하자!

import heapq


# 다른 사람의 답
def solution_another(n, edge):
    graph = [[] for _ in range(n + 1)]
    distances = [0 for _ in range(n)]
    is_visit = [False for _ in range(n)]
    queue = [0]
    is_visit[0] = True
    # 그래프 그리기
    for (a, b) in edge:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    # bfs
    while queue:
        # 선입선출☆
        i = queue.pop(0)
        for j in graph[i]:
            if not is_visit[j]:
                is_visit[j] = True
                queue.append(j)
                distances[j] = distances[i] + 1

    distances.sort(reverse=True)
    answer = distances.count(distances[0])

    return answer


# 나의 답 (dijkstra / bfs)
def solution(n, edge):

    graph = [[] for _ in range(n+1)]
    # 그래프 그리기
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    INF = int(1e9)
    distance = [INF] * (n+1)
    distance[0] = 0

    # 다익스트라
    def dijkstra(start):
        q = []
        # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
        heapq.heappush(q, (0, start))
        distance[start] = 0
        while q:  # 큐가 비어있지 않다면
            # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
            dist, now = heapq.heappop(q)
            # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
            if distance[now] < dist:
                continue
            # 현재 노드와 연결된 다른 인접한 노드들을 확인
            for i in graph[now]:
                cost = dist + 1
                # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                if cost < distance[i]:
                    distance[i] = cost
                    heapq.heappush(q, (cost, i))

    visited = [-1] * (n + 1)

    # BFS 함수 정의
    def bfs(start):
        q = [start]
        visited[start] = 0
        # q가 빌 때까지 반복
        while q:
            # 선입선출 ☆
            v = q.pop(0)
            # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
            for i in graph[v]:
                if visited[i] < 0:
                    q.append(i)
                    visited[i] = visited[v] + 1

    # 다익스트라
    dijkstra(1)
    answer_d = distance.count(max(distance))

    # BFS
    bfs(1)
    answer_b = visited.count(max(visited))

    return answer_d


print('\nanswer :', solution(6, [[3, 6], [4, 3], [3, 2],
                                 [1, 3], [1, 2], [2, 4], [5, 2]]))
