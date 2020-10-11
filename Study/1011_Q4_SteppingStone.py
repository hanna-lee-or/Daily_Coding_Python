# 프로그래머스 KAKAO 징검다리 건너기
# 징검다리를 건널 수 있는 최대 인원 수 구하기
# 디딤돌은 밟을 수 있는 횟수가 정해져 있음 stones
# 한 번에 건너뛸 수 있는 디딤돌의 최대 칸수 k
# 시간 효율성 고려 필요


# 다른 사람의 답 (이분탐색)
def isPossible(stones, k, mid):
    disappeared_stones = 0

    # mid 보다 작은 값이 k번 연속해서 나오면 건널 수 없음.
    for s in stones:
        if s - mid <= 0:
            disappeared_stones += 1
            if disappeared_stones == k:
                return False
        else:
            disappeared_stones = 0

    return True


def solution_another(stones, k):
    answer = 0

    left = 0
    right = 200000000

    # 답을 이분탐색해가며 체크함.
    while left <= right:
        mid = (left + right) // 2

        if isPossible(stones, k, mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer + 1


# 나의 답 (효율성 테스트 하나 시간초과)
def solution(stones, k):

    n = len(stones)

    first = [0, 0]
    for i in range(0, k):
        if first[1] <= stones[i]:
            first = [i, stones[i]]
    maximum = first[1]
    if maximum == 0:
        return 0

    start, end = 0, k - 1
    # start, end 구간의 최댓값들을 구함.
    # 그 최댓값 중 최소값이 정답
    while end < n - 1:
        start += 1
        end += 1
        s = stones[end]
        if first[0] == start - 1:
            first = [0, 0]
            for i in range(start, end+1):
                if first[1] <= stones[i]:
                    first = [i, stones[i]]
            if maximum > first[1]:
                maximum = first[1]
        elif s >= first[1]:
            first = [end, s]
            if maximum >= s:
                maximum = s
        if maximum == 0:
            break

    answer = maximum

    return answer


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))


