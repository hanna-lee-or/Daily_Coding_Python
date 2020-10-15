# 백준 1766 / 문제집

import sys

# 문제 수 n, 선수 문제 정보 수 m
n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n+1)]
in_degree = [0] * (n+1)
q = []
answer = []

# 그래프 그리기 + 진입차수 셋팅
for i in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    in_degree[b] += 1

for i in range(1, n+1):
    if in_degree[i] == 0:
        q.append(i)

# 선수 문제를 먼저 풀 되
# 가능한 쉬운 문제 먼저!
while q:
    q.sort(reverse=True)
    node = q.pop()
    answer.append(node)

    for g in graph[node]:
        in_degree[g] -= 1
        if in_degree[g] == 0:
            q.append(g)
print(*answer)
