# 프로그래머스 Level 3 최고의 집합
# n개의 자연수를 더해서 s가 되는 수들의 집합 중
# 곱이 가장 큰 집합. 없을 때는 -1 반환.

# n은 1이상 10,000 이하의 자연수
# s는 1이상, 100,000,000 이하의 자연수


def solution(n: int, s: int) -> list:

    # n개의 자연수를 더해서 s가 될 수 없는 경우
    if n > s:
        return [-1]
    # 모두 1이어야 s가 되는 경우
    elif n == s:
        return [1] * n

    answer = [s//n] * n

    # 골고루 배분하는게 포인트
    for i in range(s%n):
        answer[i] += 1

    return answer[::-1]


print(solution(2, 9))


