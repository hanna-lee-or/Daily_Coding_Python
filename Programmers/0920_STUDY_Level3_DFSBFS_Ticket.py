# 프로그래머스 DFS/BFS Level 3 여행경로
# 여행경로 설정하기. 간선들이 입력으로 들어옴.
# STUDY 2020/09/20

# 정답지 공부, 코드 분석
# 방향 그래프에서의 노드 탐색?


def solution(tickets):

    graph = {}  # graph = dict()

    # 그래프 만들기 (dictionary 이용)
    for a, b in tickets:
        graph[a] = graph.get(a, []) + [b]

    # 스택 이용
    # 거꾸로 정렬 => 끝에부터 pop => 알파벳 순으로 스택에 삽입
    for j in graph:
        graph[j].sort(reverse=True)

    print(graph)

    # 여행 경로 설정
    stack = ["ICN"]
    answer = []
    while stack:
        top = stack[-1]
        # 티켓의 출발지에 없거나, 해당 항공의 도착지를 다 돌았을 경우
        # => 마지막에 도달할 도착지부터 체크
        # 너가 마지막이구나!! 하는 얘들부터 넣는 방식
        if top not in graph or len(graph[top]) == 0:
            answer.append(stack.pop())
        # 도착지가 남아있을 경우
        else:
            # 탐색할 티켓을 스택에 삽입
            stack.append(graph[top][-1])
            # 해당 항공의 사용한 티켓 제거
            graph[top].pop()

    return answer[::-1]  # 배열을 거꾸로 리턴, 스택이라 거꾸로 들어가므로


print('\nanswer :', solution([["ICN", "ADK"], ["ICN", "IAD"],
                             ["IAD", "ICN"]]))

# print('\nanswer :', solution([["ICN", "JFK"], ["HND", "IAD"],
#                               ["JFK", "HND"]]))

# print('\nanswer :', solution([["ICN", "SFO"], ["ICN", "ATL"],
#                              ["SFO", "ATL"], ["ATL", "ICN"],
#                              ["ATL", "SFO"]]))
