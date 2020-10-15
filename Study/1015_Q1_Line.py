# 백준 2252 / 줄 세우기 (위상정렬)
# 위상정렬은 다양한 답을 가질 수 있으며
# 사이클이 포함되어 있다면 위상정렬은 불가능

import sys
from collections import deque

# 학생 명수 n, 키 비교한 횟수 m
n, m = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(n+1)]
in_degree = [0] * (n+1)
# 그래프 그리기 (뒤에 있을 학생 번호를 자식으로 가짐)
for i in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    in_degree[b] += 1

q = deque()
for i in range(1, n+1):
    if in_degree[i] == 0:
        q.append(i)

answer = []
while q:
    node = q.popleft()
    answer.append(node)

    for g in graph[node]:
        in_degree[g] -= 1
        if in_degree[g] == 0:
            q.append(g)
print(*answer)
