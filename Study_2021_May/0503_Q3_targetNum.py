# 프로그래머스 Level2 타겟 넘버 (DFS/BFS)
# numbers 원소를 적절히 더하거나 빼서
# 타겟 넘버를 만들 수 있는 경우의 수

# 숫자는 2개 이상 20개 이하
# 각 숫자는 1 이상 50 이하
# 타겟 넘버는 1 이상 1000 이하


# 다른 사람의 답 관련 import
from itertools import product


# 나의 답.
def solution(numbers, target):

    if len(numbers) == 1:
        if numbers[-1] == abs(target):
            return 1
        else:
            return 0

    n = numbers[-1]

    return solution(numbers[:-1], target+n) + solution(numbers[:-1], target-n)


print(solution([1, 1, 1, 1, 1], 3))  # 5


# 다른 사람의 답.
# list(map(함수, 리스트)) / tuple(map(함수, 튜플))
# 원소에 대해 지정된 함수를 적용시킴.
# product 함수 (곱집합 : 여러 집합들 간에 하나씩 뽑아 조합을 만들 수 있는 모든 수)
def solution_another(numbers, target):
    l = [(x, -x) for x in numbers]
    # product 로 모든 조합을 구하고, sum 으로 각 조합의 합을 구함.
    s = list(map(sum, product(*l)))
    return s.count(target)


print(solution_another([1, 1, 1, 1, 1], 3))  # 5
