# 네이버 코딩테스트 2
# Hanna 2020/09/26

# 메모


from itertools import combinations


def solution(n, edges):
    answer = []

    # 특정 원소가 속한 집합을 찾기
    def find_parent(parent, x):
        # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
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

    # 노드의 개수와 간선(Union 연산)의 개수 입력 받기
    v, e = n, len(edges)
    parent = [0] * v  # 부모 테이블 초기화하기

    # 2개의 간선 없애기
    index = [i for i in range(e)]
    remove_list = list(combinations(index, 2))
    print("r :", remove_list)

    flag = 0
    while flag < len(remove_list):

        # 부모 테이블상에서, 부모를 자기 자신으로 초기화
        for i in range(0, v):
            parent[i] = i

        # Union 연산을 각각 수행
        for i in range(e):
            if i != remove_list[flag][0] and i != remove_list[flag][1]:
                a, b = edges[i]
                union_parent(parent, a, b)

        # 각 원소가 속한 집합 출력하기
        print(remove_list[flag], ': ', end='')
        node = set()
        for i in range(0, v):
            node.add(parent[i])
            print(parent[i], end=' ')
        print(" ", node)

        temp = parent.count(node.pop())
        flagT = False
        while node:
            if temp != parent.count(node.pop()):
                flagT = True

        if not flagT:
            answer.append(remove_list[flag][0])
            answer.append(remove_list[flag][1])
            break

        flag += 1

    return answer


print('\nanswer :', solution(9, [[0, 2], [2, 1], [2, 4], [3, 5],
                                 [5, 4], [5, 7], [7, 6], [6, 8]]))

