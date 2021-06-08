# 프로그래머스 Level2 가장 큰 수
# 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
# [6, 10, 2] => 6210

# numbers 의 길이 : 100,000 이하
# numbers 의 원소 : 1,000 이하
# 문자열로 바꾸어 return

import pprint
import math
from collections import defaultdict
import functools


# 나의 답안. key=lambda x: x*3 부분 외부 참고.
def solution(numbers):

    numbers = [str(n) for n in numbers]
    # num 은 1000 이하의 수이므로 3자리수로 맞춘 뒤 비교
    numbers.sort(key=lambda x: x*3, reverse=True)
    print(numbers)

    # 000 같은 경우 0으로 출력하기 위해 int 변환 후 str 변환
    return str(int(''.join(numbers)))


print(solution([6, 10, 2]))  # "6210"
print(solution([3, 30, 34, 5, 9]))  # "9534330"


# 다른 사람의 풀이. 정렬 key 함수를 정의한 것이 핵심!
def comparator(a, b):
    t1 = a+b
    t2 = b+a
    #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0
    return (int(t1) > int(t2)) - (int(t1) < int(t2))


def solution_another(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator), reverse=True)
    answer = str(int(''.join(n)))
    return answer
