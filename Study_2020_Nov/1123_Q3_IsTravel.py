# 백준 1976 / 여행 가자
# 여행이 가능한지 여부 판단

"""
3
3
0 1 0
1 0 1
0 1 0
1 2 3

Answer : YES
"""


import sys


# 도시 수 N, 여행 계획에 속한 도시 수 M
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

graph = []
visited = [False] * n
group = [i for i in range(n)]
# 도시 연결 정보 입력받기
for _ in range(n):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    graph.append(row)

# 여행 계획 정보 입력받기
plan = list(map(int, sys.stdin.readline().rstrip().split()))


# DFS 그룹 짓기
def dfs(start, group_num):
    # 방문 처리 및 그룹 넘버 체킹
    visited[start] = True
    group[start] = group_num
    
    for v in range(n):
        # 방문하지 않은 이웃 도시
        if graph[start][v] == 1 and not visited[v]:
            dfs(v, group_num)


# 도시를 돌며 그룹을 체킹한다.
for i in range(n):
    if not visited[i]:
        dfs(i, i)

# 여행 계획에 있는 도시들이 같은 그룹이면 OK
gn = group[plan[0]-1]
flag = True
for city in plan:
    # 다른 그룹이 존재할 경우
    if group[city-1] != gn:
        flag = False
        print("NO")
        break

# 모두 같은 그룹이면
if flag:
    print("YES")


print(graph)
print(plan)
print(visited)
print(group)
