# 프로그래머스 힙(Heap) Level 3 디스크 컨트롤러
# 평균 처리 속도의 최소값
# Hanna 2020/09/30

# 한 번에 하나의 요청, 요청받은 순서대로
# 특정 작업의 처리 속도는 요청시간~종료시간 (대기시간 포함)

# 요청이 한동안 없다가 들어온 경우
# 시간 포인터(end)를 해당 요청 시간으로 셋팅
# 위 경우를 놓쳐서 30분정도 헤멨다 ㅎㅎ;;

import heapq
import math


# 나의 답
def solution(jobs):

    jobs.sort(reverse=True)
    print(jobs)
    q = []
    n = len(jobs)
    time = 0
    end = 0

    while True:
        # 요청(q)이 없는 경우
        if not q:
            if not jobs:
                break
            else:
                # 요청이 한동안 없다가 들어온 경우
                # 시간 포인터(end)를 해당 요청 시간으로 셋팅☆
                a, b = jobs.pop()
                end = a
                heapq.heappush(q, [b, a])
        # 들어온 요청(q) 중 가장 짧은 작업 수행
        j, i = heapq.heappop(q)
        end += j
        time += end - i
        print([i, j], ":", end - i, "(", end, ")")
        # 작업 진행 중에 들어온 요청은 heap 에 넣기
        while len(jobs) != 0 and jobs[-1][0] <= end:
            a, b = jobs.pop()
            heapq.heappush(q, [b, a])

    answer = math.floor(time/n)

    return answer


print('\nanswer :', solution([[0, 1], [0, 2], [5, 1]]))

