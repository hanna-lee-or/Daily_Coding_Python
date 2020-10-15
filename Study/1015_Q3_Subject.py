# 백준 14567 / 선수과목
# 한 학기에 들을 수 있는 과목 수에는 제한이 없다.
# 모든 과목은 매 학기 항상 개설된다.

import sys
from collections import deque

# 과목 수 n, 선수 조건 수 m
n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n+1)]
in_degree = [0] * (n+1)
q = deque()
answer = [0] * n

# 그래프 그리기 + 진입차수 셋팅
for i in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    in_degree[b] += 1

for i in range(1, n+1):
    if in_degree[i] == 0:
        q.append(i)
        answer[i-1] = 1

# 선수 문제를 먼저 풀 되
# 가능한 쉬운 문제 먼저!
while q:
    node = q.popleft()

    for g in graph[node]:
        in_degree[g] -= 1
        if in_degree[g] == 0:
            q.append(g)
            answer[g - 1] = answer[node - 1] + 1
print(*answer)
