# 프로그래머스 Heap Level 3 야근 지수
# Hanna 2020/10/16

# 야근 피로도는 야근을 시작한 시점에서 남은 일의 작업량을 제곱하여 더한 값.
# 야근 피로도를 최소화한 값은?

# 아이디어는 떠올렸으나 힙을 떠올리지 못함.
# => 답지 참고함.

import heapq


def solution(n, works):

    # 힙은 기본적으로 최소값을 반환.
    # 최대값을 반환하기 원하므로 음수화.
    for i in range(len(works)):
        works[i] *= -1

    # 힙 생성
    heapq.heapify(works)

    # 최댓값 -1 작업을 n만큼 수행함.
    for i in range(n):
        m = heapq.heappop(works)
        if m >= 0:
            break
        m += 1
        heapq.heappush(works, m)

    answer = 0
    for w in works:
        answer += w * w

    return answer


print('\nanswer :', solution(1, [2, 1, 2]))
