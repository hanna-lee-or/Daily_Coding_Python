# 프로그래머스 Level 3 단어 변환
# begin이 target이 되도록 변환
# 가장 짧은 변환의 길이 (복습)


from collections import defaultdict
from collections import deque


def solution(begin: str, target: str, words: str) -> int:

    if target not in words:
        return 0

    n = len(words)
    m = len(words[0])

    # 단어 그래프 만들기 (한 글자 차이면 인접 노드인 거임!)
    graph = defaultdict(list)

    # 최단 거리 테이블
    INF = int(1e9)
    distance = dict()

    # begin 단어랑 words 내 단어 비교
    for w in words:
        distance[w] = INF
        for k in range(m):
            # 한 글자 차이면 인접 노드로 표시
            if begin[:k] + begin[k+1:] == w[:k] + w[k+1:]:
                graph[begin].append(w)
                break

    # words 내 단어 두 개씩 비교
    for i in range(n):
        a = words[i]
        for j in range(i+1, n):
            b = words[j]
            for k in range(m):
                # 한 글자 차이면 인접 노드로 표시
                if a[:k] + a[k+1:] == b[:k] + b[k + 1:]:
                    graph[a].append(b)
                    graph[b].append(a)
                    break

    def dijkstra(start, end):
        q = deque()
        q.append(start)

        # 인접 노드로 뻗어가며 거리 체크
        flag = False
        while q:
            node = q.popleft()
            # 거리 설정
            if not flag:
                flag = True
                dist = 1
            else:
                dist = distance[node] + 1
            # 이웃 노드 방문, 거리 체크
            for v in graph[node]:
                if distance[v] == INF:
                    q.append(v)
                    distance[v] = dist
                else:
                    distance[v] = min(distance[v], distance[node] + 1)

    answer = 0
    dijkstra(begin, target)
    # 변환할 수 없는 경우, 0 반환
    if distance[target] == INF:
        answer = 0
    else:
        answer = distance[target]

    return answer


# 답 4
print(solution("hit", "cog", ["hot", "dot", "dog",
                              "lot", "log", "cog"]))


