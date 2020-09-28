# 프로그래머스 깊이/너비 우선 탐색(BFS/DFS) Level 3 단어 변환
# 한 번에 한 개의 알파벳씩, words에 있는 단어로만 변환.
# 최소 몇 단계 과정을 거쳐야 begin에서 target으로 변환할 수 있는가.
# Hanna 2020/09/28

# 다익스트라 알고리즘 사용 (간선 간 거리는 1로 취급)

from collections import defaultdict
import heapq


def solution(begin, target, words):
    
    if target not in words:
        return 0

    words.sort()

    n = len(words)
    m = len(words[0])
    # 단어 그래프 만들기
    graph = defaultdict(list)
    INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정
    # 최단 거리 테이블
    distance = {}
    # 시작 단어랑 체크
    for w in words:
        distance[w] = INF
        for i in range(m):
            if begin[:i] == w[:i] and begin[i+1:] == w[i+1:]:
                graph[begin].append(w)
                break
    # 두 단어씩 체크
    for a in range(n):
        for b in range(a+1, n):
            word_a = words[a]
            word_b = words[b]
            # 한 글자만 다른지 체크
            for i in range(m):
                if word_a[:i] == word_b[:i] and word_a[i+1:] == word_b[i+1:]:
                    graph[word_a].append(word_b)
                    graph[word_b].append(word_a)
                    break
    print(graph)

    def dijkstra(start, graph):
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

    answer = 0
    # 다익스트라 알고리즘을 수행
    dijkstra(begin, graph)
    print(distance)

    if distance[target] == INF:
        answer = 0
    else:
        answer = distance[target]

    return answer


print('\nanswer :', solution("hit", "cog", ["hot", "dot", "dog",
                                            "lot", "log", "cog"]))
