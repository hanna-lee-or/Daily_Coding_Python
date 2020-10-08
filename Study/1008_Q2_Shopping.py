# 프로그래머스 KAKAO 보석 쇼핑
# 모든 종류의 보석을 포함하는 가장 짧은 구간 찾기

# 미완

from collections import defaultdict


def solution(gems):
    
    info = defaultdict(list)
    
    for i, g in enumerate(gems):
        if g in info.keys():
            if len(info[g]) >= 2:
                info[g][1] = i
            else:
                info[g].append(i)
        else:
            info[g].append(i)

    print(info)

    area = info.values()
    count = 0
    right = []
    left = []
    for a in area:
        right.append(a[-1])
        left.append(a[0])
    
    count = max(right) - min(left)
    print(min(left), max(right))
    count = min(right) - min(left)
    print(min(right), max(left))

    answer = []

    return answer


print(solution(["AA", "AB", "AC", "AA", "AC"]))


"""
    check = list(product(*jewel))
    minimum = 1e9
    for c in check:
        a = min(c)
        b = max(c)
        if b - a < minimum:
            minimum = b - a
            answer = [a + 1, b + 1]
"""
