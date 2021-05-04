# 프로그래머스 Level2 뉴스 클러스터링
# 자카드 유사도는 집합 간의 유사도를 검사하는 여러 방법 중의 하나

# 각 문자열의 길이는 2 이상, 1,000 이하
# 입력으로 들어온 문자열은 두 글자씩 끊어서 다중집합의 원소로 만든다. (중복 허용)
# 영문자로 된 글자 쌍만 유효하고, 기타 공백이나 숫자, 특수 문자는 무시한다.
# 다중집합 원소 사이를 비교할 때, 대문자와 소문자의 차이는 무시한다.
# 65536을 곱한 후에 소수점 아래를 버리고 정수부만 출력

import re
import math

from collections import Counter


# 나의 답. 정규식 활용.
def solution(str1, str2):

    str1 = makeList(str1)
    str2 = makeList(str2)
    print(str1)
    print(str2)

    if not str1 and not str2:
        return 65536
    elif not str1 or not str2:
        return 0

    an = len(str1) - 1
    bn = len(str2) - 1
    i = j = 0

    # 교집합 개수 구하기
    count = 0
    while i <= an and j <= bn:
        if str1[i] == str2[j]:
            count += 1
            i += 1
            j += 1
        elif str1[i] < str2[j]:
            i += 1
        else:
            j += 1

    # 유사도는 (교집합 개수 / (A 개수 + B 개수) - 교집합 개수)
    # 유사도는 0~1 이므로 65536 곱한 후 정수부 출력
    print(f"count: {count} , answer: {count/(an+bn+2-count)}")
    return int(count/(an+bn+2-count) * 65536)


def makeList(l) -> list:

    p = re.compile('[a-zA-Z]{2}')

    new_l = []
    n = len(l) - 1
    for i in range(n):
        s = l[i:i+2]
        if p.match(s):
            new_l.append(s.lower())
    new_l.sort()
    return new_l


# print(solution("FRANCE", "french"))  # 16384
# print(solution("handshake", "shake hands"))  # 65536
# print(solution("aa1+aa2", "AAAA12"))  # 43690
print(solution("E=M*C^2", "e=m*c^2"))  # 65536


# 다른 사람의 풀이.
def solution_another(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    # 집합을 활용하면 중복 원소가 무시된다.
    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    # 따라서 A, B 집합에서 교집합 원소와 매칭되는 원소 개수를 카운트해
    # 문제에서 원하는 교집합 원소 개수를 카운트한다.
    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)


# 다른 사람의 풀이. 카운터 활용. isalpha 함수 활용.
def solution_plus(str1, str2):
    # make sets
    s1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    s2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    if not s1 and not s2:
        return 65536
    c1 = Counter(s1)
    c2 = Counter(s2)
    # 카운터의 intersect, union 활용.
    answer = int(float(sum((c1&c2).values()))/float(sum((c1|c2).values())) * 65536)
    return answer
