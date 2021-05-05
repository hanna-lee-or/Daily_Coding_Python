# 프로그래머스 Level2 튜플
# 중복되는 원소가 없는 튜플을 집합 기호 '{', '}'를 이용해 표현할 수 있다.
# {{a1}, {a1, a2}, {a1, a2, a3}, ... {a1, a2, a3, a4, ..., an}}
# 이 때, 튜플은 원소 순서가 중요하나 집합 표현 시엔 원소의 순서가 바뀌어도 상관없다.

# 특정 튜플을 표현하는 집합이 담긴 문자열 s가 매개변수로 주어질 때,
# s가 표현하는 튜플을 배열에 담아 return 하라.

# s의 길이는 5 이상 1,000,000 이하. 숫자와 { } , 으로만 이루어져 있다.
# s가 표현하는 튜플의 원소는 1 이상 100,000 이하.
# return 하는 배열의 길이가 1 이상 500 이하인 경우만 입력으로 주어진다.

import re
import math

from collections import Counter


# 나의 답. 정규식 & 카운터 사용.
def solution(s):
    answer = []

    p = re.compile(r"\d+")
    m = Counter(p.findall(s))

    for num in m.most_common():
        answer.append(int(num[0]))

    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))  # [2, 1, 3, 4]
# print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))  # [2, 1, 3, 4]
# print(solution("{{20,111},{111}}"))  # [111, 20]
# print(solution("{{123}}"))  # [3, 2, 4, 1]


# 다른 사람의 답.
def solution(s):

    s = Counter(re.findall(r'\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(),
                                               key=lambda x: x[1],
                                               reverse=True)]))
