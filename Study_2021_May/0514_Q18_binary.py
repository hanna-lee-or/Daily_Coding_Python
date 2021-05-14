# 프로그래머스 Level2 이진 변환 반복하기
# 0과 1로 이루어진 어떤 문자열 x에 대한 이진 변환을 다음과 같이 정의합니다.
#   ㄴ x의 모든 0 제거 => x의 길이를 c라 할 때, x를 "c를 2진법으로 표현한 문자열"로 변환
# (ex. "0111010" -> "1111" -> "100")
# s가 "1"이 될 때까지 계속해서 s에 이진 변환을 가했을 때,
# 이진 변환의 횟수와 변환 과정에서 제거된 모든 0의 개수를 각각 배열에 담아 return

# s의 길이는 1 이상 150,000 이하
# s에는 '1'이 최소 하나 이상 포함

import pprint


# 나의 답안.
def solution(s):

    t = 0
    r = 0
    while s != "1":
        t += 1
        count = 0
        for c in s:
            if c == "0":
                count += 1
        s = makeBinary(len(s) - count)
        r += count

    return [t, r]


def makeBinary(num) -> str:

    s = ""
    while num > 0:
        num, r = divmod(num, 2)
        s += str(r)

    return s[::-1]


print(solution("110010101001"))  # [3, 8]
print(solution("01110"))  # [3, 3]
print(solution("1111111"))  # [4, 1]


# 다른 사람의 풀이.
def solution(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:]
    return [a, b]
