# 프로그래머스 Level 3 네트워크
# 네트워크 수 (복습)


def solution(n: int, computers: list) -> int:

    # n은 노드 개수, computers는 인접 행렬 방식의 그래프
    visited = [False] * n

    # DFS 함수
    def dfs(start):

        visited[start] = True

        for i, is_connect in enumerate(computers[start]):
            # 이웃 노드 중 방문하지 않은 곳이면
            if not visited[i] and is_connect == 1:
                dfs(i)

    # 네트워크 수 세기
    count = 0
    for i in range(n):
        # 방문 처리가 안 된 노드면 DFS 실행
        if not visited[i]:
            count += 1
            dfs(i)

    return count


# print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))

