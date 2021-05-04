# 프로그래머스 Level2 더 맵게 (힙)
# 매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶다.
# 이를 위해 가장 낮은 두 개의 음식을 섞어 새로운 음식을 만든다.
# 섞은 음식의 스코빌 지수 = 가장 안 매운 음식의 스코빌 지수 + (두 번째 스코빌 지수 * 2)
# Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞는다.
# 섞어야 하는 최소 횟수를 return 하라. 만들 수 없는 경우에는 -1 을 return.

# scoville의 길이는 2 이상 1,000,000 이하
# K는 0 이상 1,000,000,000 이하
# scoville의 원소는 각각 0 이상 1,000,000 이하


import heapq

# 나의 답. 힙 사용.
def solution(scoville, K):

    heapq.heapify(scoville)

    count = 0
    while scoville:
        a = heapq.heappop(scoville)
        if a >= K:
            return count
        if not scoville:
            break
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + b * 2)
        count += 1

    return -1


print(solution([1, 2, 3, 9, 10, 12], 7))  # 2


