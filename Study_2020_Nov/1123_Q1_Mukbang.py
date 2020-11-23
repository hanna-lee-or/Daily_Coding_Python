# 프로그래머스 Level 4 Kakao 무지의 먹방 라이브

# 무지는 다음과 같은 방법으로 음식을 섭취한다.
# - 무지는 1번 음식부터 먹기 시작하며,
#   회전판은 번호가 증가하는 순서대로 음식을 무지 앞으로 가져다 놓는다.
# - 마지막 번호의 음식을 섭취한 후에는 회전판에 의해
#   다시 1번 음식이 무지 앞으로 온다.
# - 무지는 음식 하나를 1초 동안 섭취한 후 남은 음식은 그대로 두고,
#   다음 음식을 섭취한다.
# - 다음 음식이란, 아직 남은 음식 중 다음으로 섭취해야 할
#   가장 가까운 번호의 음식을 말한다.
# - 회전판이 다음 음식을 무지 앞으로 가져오는데 걸리는 시간은 없다고 가정한다.

# 먹방을 시작한 지 K 초 후에 네트워크 장애로 인해 방송이 잠시 중단되었다.
# 무지는 네트워크 정상화 후 다시 방송을 이어갈 때,
# 몇 번 음식부터 섭취해야 하는지를 알고자 한다.

# 각 음식을 모두 먹는데 필요한 시간이 담겨있는 배열 food_times,
# 네트워크 장애가 발생한 시간 K 초가 매개변수로 주어질 때
# 몇 번 음식부터 다시 섭취하면 되는지 return (없으면 -1)

# 힙을 사용한다는 아이디어까진 도출했지만
# 나머지는 답지 참고..ㅠㅠ

import heapq


def solution(food_times: list, k: int) -> int:

    n = len(food_times)

    # 우선순위 큐에 시간 넣기
    for i, t in enumerate(food_times):
        food_times[i] = (t, i)
    heapq.heapify(food_times)

    small_food = food_times[0][0]
    prev_food = 0
    # 작은 음식을 완전히 소비하기 위해 원판을 완주할 수 있는 경우
    while k - ((small_food - prev_food) * len(food_times)) >= 0:
        # 해당 음식을 완전히 소비하는 데 걸린 시간만큼 뺀다.
        k -= (small_food - prev_food) * len(food_times)
        prev_food, index = heapq.heappop(food_times)
        if not food_times:
            return -1
        small_food = food_times[0][0]
    food_times = sorted(food_times, key=lambda x: x[1])

    return food_times[k % len(food_times)][1] + 1


# print(solution([3, 1, 2], 5))
print(solution([4, 2, 3, 6, 7, 1, 5, 8], 16))

