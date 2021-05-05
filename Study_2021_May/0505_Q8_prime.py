# 프로그래머스 Level2 소수 찾기
# 한자리 숫자가 적힌 종이 조각이 흩어져있다.
# 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 한다.

# numbers는 길이 1 이상 7 이하인 문자열
# "013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미

from itertools import permutations


# 나의 답. 순열 사용.
def solution(numbers):

    # 수를 배치시킨다.
    num_set = set()
    max_len = len(numbers) + 1
    for l in range(1, max_len):
        for x in permutations(numbers, l):
            num_set.add(int(''.join(x)))

    num_set -= set(range(0, 2))

    # 소수인지 판별한다.
    count = 0
    for n in num_set:
        prime_flag = True
        for i in range(2, int(n / 2) + 1):
            if n % i == 0:
                prime_flag = False
                break
        if prime_flag:
            count += 1
            print(n)

    return count


# print(solution("17"))  # 3
print(solution("011"))  # 2


# 다른 사람의 답. 에라토스테네스 체 (범위에서 합성수를 지우는 방식으로 소수를 찾는 방법) 활용.
def solution_another(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    # 합성수를 지워나간다.
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    # 집합에 남아있는 수들이 소수이다.
    return len(a)
