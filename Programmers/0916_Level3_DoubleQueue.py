# 프로그래머스 DFS/BFS Level 3 이중우선순위큐
# 이중우선순위큐 [I 숫자 (입력), D 1 (최댓값 제거), D -1 (최솟값 제거)]
# Hanna 2020/09/16

# heapq 사용해서도 풀 수 있음


def solution(operations):
    q = []

    for query in operations:
        op, data = query.split()
        data = int(data)
        if op == 'I':
            q.append(data)
            q.sort()
        else:
            # 제거 연산은 리스트에 데이터가 있는 경우에만
            if q:
                # 연산 명령에 따라 최대 or 최소 제거
                if data == 1:
                    q.pop()
                else:
                    q.pop(0)

    # 최대, 최소값 넣기
    if len(q) == 0:
        answer = [0, 0]
    else:
        answer = [q[-1], q[0]]

    return answer


print('\nanswer :', solution(["I 1", "I 2", "I 3", "I 4", "I 5",
                              "I 6", "I 7", "I 8", "I 9", "I 10",
                              "D 1", "D -1", "D 1", "D -1", "I 1",
                              "I 2", "I 3", "I 4", "I 5", "I 6",
                              "I 7", "I 8", "I 9", "I 10", "D 1",
                              "D -1", "D 1", "D -1"]))
