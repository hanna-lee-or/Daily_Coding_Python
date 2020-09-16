# 프로그래머스 이분탐색 Level 3 입국심사
# 입국심사를 기다리는 사람 n명, 각 심사관의 심사 시간 times
# 모든 사람이 심사를 받는데 걸리는 시간은?
# Hanna 2020/09/16

# 이분탐색 아이디어 활용하기!


def solution(n, times):
    answer = 0

    times.sort()

    start = 0
    end = times[-1] * n
    # 시간을 반씩 줄여가며 최적의 해를 찾는다.
    while start <= end:
        target_time = (start + end) // 2
        rest_n = n
        flag = False
        for t in times:
            tn = target_time // t
            rest_n -= tn
            if rest_n <= 0:
                flag = True
                break
        if flag:
            answer = target_time
            end = target_time - 1
        else:
            start = target_time + 1

    return answer


print('\nanswer :', solution(6, [7, 10]))
