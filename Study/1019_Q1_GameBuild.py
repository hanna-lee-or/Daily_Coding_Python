# 백준 1516 / 게임 개발
# Hanna 2020/10/19

# 각 건물이 완성되기까지 걸리는 최소 시간

import sys
from collections import deque

# 건물의 종류 수 N
N = int(sys.stdin.readline().rstrip())

# 각 건물을 짓는데 걸리는 시간, 먼저 지어져야 하는 건물들의 번호
# 각 줄은 -1로 끝남.
time = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
q = deque()
degree = [0 for _ in range(N+1)]
for i in range(1, N+1):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    time[i] = temp[0]
    for j in range(1, len(temp) - 1):
        graph[temp[j]].append(i)
        degree[i] += 1

for i in range(1, N+1):
    if degree[i] == 0:
        q.append(i)

min_time = [0] * (N+1)
while q:
    node = q.popleft()
    min_time[node] += time[node]

    for g in graph[node]:
        # 이 부분 조심하기! 건물은 동시에 올려질 수 있음.
        # 따라서 부모 건물 중 늦게 끝나는 시간을
        # 자식 건물이 가져가야 함.
        if min_time[g] < min_time[node]:
            min_time[g] = min_time[node]
        degree[g] -= 1
        if degree[g] == 0:
            q.append(g)

print(time)
print(graph)
print(degree)
for i in range(1, N+1):
    print(min_time[i])
