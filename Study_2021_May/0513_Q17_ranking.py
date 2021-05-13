# 프로그래머스 Level2 순위 검색
# 지원자는 지원서 작성 시 아래와 같이 4가지 항목을 반드시 선택하도록 하였습니다.
# 개발언어 (cpp, java, python) / 지원 직군 (backend, frontend) /
# 경력구분 (junior, senior) / 소울푸드 (chicken, pizza)
# 지원자들의 지원 조건을 선택하면 해당 조건에 맞는 지원자가
# 몇 명인 지 쉽게 알 수 있는 도구를 만들고 있습니다.
# (ex. "- and - and - and - 150" : 코딩테스트 점수가 150점 이상인 지원자)

# info 배열의 크기는 1 이상 50,000 이하
#   ㄴ "개발언어 직군 경력 소울푸드 점수" 형식
# query 배열의 크기는 1 이상 100,000 이하
#   ㄴ "[조건] X" 형식으로, '-' 표시는 해당 조건을 고려하지 않겠다는 의미

import pprint
import re

from functools import reduce
from collections import defaultdict
from bisect import insort, bisect_left


# 나의 답안. 효율성 통과 X.
def solution(info, query):
    answer = []
    info = [[getDataCode(data), int(data[-1])]
            for data in list(map(lambda x: x.split(), info))]
    info.sort(key=lambda x: x[-1], reverse=True)
    # pprint.pprint(info)

    for q in query:
        q = list(filter(lambda x: x != "and", q.split()))
        q = [getDataCode(q), int(q[-1])]
        p = re.compile(q[0])
        # 쿼리 조건과 일치하는 데이터 개수 카운트
        count = 0
        for data in info:
            if data[-1] >= q[-1]:
                if re.match(p, data[0]):
                    count += 1
            else:
                break
        answer.append(count)

    return answer


def getDataCode(data) -> str:
    language, job, history, food, score = data
    code = ""
    # 언어
    if language == "cpp":
        code += "1"
    elif language == "java":
        code += "2"
    elif language == "python":
        code += "4"
    else:
        code += "."
    # 직군
    if job == "backend":
        code += "1"
    elif job == "frontend":
        code += "2"
    else:
        code += "."
    # 경력
    if history == "junior":
        code += "1"
    elif history == "senior":
        code += "2"
    else:
        code += "."
    # 소울푸드
    if food == "chicken":
        code += "1"
    elif food == "pizza":
        code += "2"
    else:
        code += "."

    return code


print(solution(["java backend junior pizza 150", "python frontend senior chicken 210",
                "python frontend senior chicken 150", "cpp backend senior pizza 260",
                "java backend junior chicken 80", "python backend senior chicken 50"],
               ["java and backend and junior and pizza 100",
                "python and frontend and senior and chicken 200",
                "cpp and - and senior and pizza 250",
                "- and backend and senior and - 150",
                "- and - and - and chicken 100",
                "- and - and - and - 150"]))
# [1,1,1,1,2,4]


# 다른 사람의 풀이. 24 개의 조합 => 데이터 구조화를 통해 info 범위 줄이기.
# https://github.com/yuneg11/Programmers-Solutions/tree/master/solutions/72412%20-%20순위%20검색
# bit mask 로 비트 연산하여 조건 일치 판별.
# bisect 모듈을 활용하여 점수 정렬 및 개수 카운트
def solution_another(info, query):
    table = {"c": 3, "j": 5, "p": 6, "b": 6, "f": 5, "s": 6, "-": 0}
    conv = lambda l, t: (reduce(lambda a, k: (a << 3) + t(table[k[0]]), l[:-1], 0), int(l[-1]))
    # 7 - x = bit field 에 해당 / table 은 bit mask 에 해당
    info = list(map(lambda s: conv(s.split(" "), lambda x: 7 - x), info))
    print(info)
    query = list(map(lambda s: conv([c for c in s.split(" ") if c != "and"], lambda x: x), query))
    print(query)
    d = defaultdict(list)
    for k, v in info:
        insort(d[k], v)
    print(d)
    # bit field & bit mask == 0 이면 조건이 일치하는 것. (k & q == 0)
    # l 은 dictionary 아이템 리스트. 점수 오름차순으로 정렬되어 있으므로
    # bisect_left 를 통해 v 점수 이상인 데이터의 개수를 셀 수 있음.
    return [sum([len(l) - bisect_left(l, v) for k, l in d.items() if not k & q]) for q, v in query]


"""
(조건의 경우의 수 C, info의 길이 N)

info의 관점에서 info 구조화
  - 시간 복잡도: O(C x N)
  - 공간 복잡도: O(N)
query의 관점에서 info 구조화
  - 시간 복잡도: O(N)
  - 공간 복잡도: O(C x N)
"""

"""
(bit field 와 bit mask 동작)

a = 001 010 010 010 = 658 // ["cpp", "frontend", "junior",  "pizza" ]
b = 000 101 000 110 = 326 // [ "-" , "frontend",    "-"  , "chicken"]
a & b = 000 000 000 010 =   2 // [ true,    true   ,   true  ,   false  ]
"""

print(solution_another(["java backend junior pizza 150", "python frontend senior chicken 210",
                        "python frontend senior chicken 150", "cpp backend senior pizza 260",
                        "java backend junior chicken 80", "python backend senior chicken 50"],
                       ["java and backend and junior and pizza 100",
                        "python and frontend and senior and chicken 200",
                        "cpp and - and senior and pizza 250",
                        "- and backend and senior and - 150",
                        "- and - and - and chicken 100",
                        "- and - and - and - 150"]))
# [1,1,1,1,2,4]
