# 프로그래머스 Level1 폰켓몬
# N/2 마리의 폰켓몬을 고를 때
# 얻을 수 있는 폰켓몬의 최대 종류 수


#
def solution(nums):
    answer = 0

    half_n = int(len(nums) / 2)
    kinds = set(nums)
    k = len(kinds)

    if k >= half_n:
        return half_n
    else:
        return k


print(solution([3, 1, 2, 3]))


# 다른 사람의 풀이. min() 함수의 간결함이 포인트.
def solution_another(ls):
    return min(len(ls)/2, len(set(ls)))
