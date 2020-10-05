# 프로그래머스 월간 코드 챌린지 1 두 개 뽑아서 더하기
# 두 수를 조합하여 만들 수 있는 덧셈 결과 오름차순

from itertools import combinations


def solution(numbers):

    answer = []

    two = list(combinations(numbers, 2))
    add = set()

    for t in two:
        a, b = t
        add.add(a+b)

    for n in add:
        answer.append(n)

    answer.sort()

    return answer


print(solution([2, 1, 3, 4, 1]))
