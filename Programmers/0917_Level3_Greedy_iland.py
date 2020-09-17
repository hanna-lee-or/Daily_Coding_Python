# 프로그래머스 Greedy Level 3 섬 연결하기
# 섬 연결 최소 비용 구하기
# Hanna 2020/09/17


# 신장 그래프, 크루스칼 알고리즘


def solution(n, costs):
    answer = 0

    # 특정 원소가 속한 집합을 찾기
    def find_parent(parent, x):
        # 루트 노드는 자기자신을 부모로 갖는 노드
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]

    # 두 원소가 속한 집합을 합치기
    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    # 노드, 간선 개수
    v, e = n, len(costs)

    # 부모 테이블상에서, 부모를 자기 자신으로 초기화
    parent = [0] * (v + 1)
    for i in range(1, v + 1):
        parent[i] = i

    # 간선 비용 순으로 정렬
    costs.sort(key=lambda x: x[2])

    # 간선을 하나씩 확인하며 (크루스칼 알고리즘)
    for edge in costs:
        a, b, cost = edge
        # 사이클이 발생하지 않는 경우에만 집합에 포함
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += cost

    return answer


print('\nanswer :', solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5],
                                 [1, 3, 1], [2, 3, 8]]))
