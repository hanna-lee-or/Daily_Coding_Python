# 프로그래머스 DFS/BFS Level 3 네트워크
# 네트워크 수 구하기 (이어져 있으면 같은 큐)
# Hanna 2020/09/16

# 책과 다르게 문제의 입력이
# 인접 리스트가 아닌 "인접 행렬"로 들어온다는 점 유의!


def solution(n, computers):

    # DFS 함수 정의
    def dfs(graph, start, visited):
        # 현재 노드를 방문 처리
        visited[start] = True
        # print(start, end=' ')
        # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
        for i, v in enumerate(graph[start]):
            if v == 1 and not visited[i]:
                dfs(graph, i, visited)

    # DFS 함수 정의 (Another)
    def dfs_plus(computers, start, visited):
        stack = [start]
        while stack:
            j = stack.pop()
            if visited[j] == 0:
                visited[j] = 1
                # print(j, end=' ')
            for i, v in enumerate(computers[j]):
                if v == 1 and not visited[i]:
                    stack.append(i)
        # print()

    # 각 노드가 방문된 정보
    visited = [False] * n
    # bfs 시작점
    idx = 0
    # 네트워크 수
    answer = 0

    # 모든 노드가 방문 처리 될 때까지 반복
    while True:
        if visited[idx] == 0:
            # 재귀 dfs가 더 빠르다
            dfs(computers, idx, visited)
            # dfs_plus(computers, idx, visited)
            answer += 1
        idx += 1
        if idx >= n:
            break
    return answer



print('\nanswer :', solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))

