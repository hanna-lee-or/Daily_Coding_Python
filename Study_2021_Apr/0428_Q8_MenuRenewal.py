# 프로그래머스 Level2 메뉴 리뉴얼
# 이전에 각 손님들이 주문할 때 가장 많이 함께 주문한 단품메뉴들을
# 코스요리 메뉴로 구성하기로 했습니다.
# 코스요리 메뉴는 최소 2가지 이상의 단품메뉴로 구성.
# 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 후보 포함.

# orders 배열의 크기는 2 이상 20 이하입니다.
# orders 배열의 원소는 크기가 2 이상 10 이하입니다.
# course 배열의 크기는 1 이상 10 이하입니다.

from collections import Counter
import collections
import itertools


def solution(orders, course):
    answer = []

    order_len = [[] for _ in range(11)]
    for i, o in enumerate(orders):
        order_len[len(o)].append(i)

    print(f"order_len : {order_len}")

    for count in course:
        combis = []
        for order_list in order_len[count:]:
            if len(order_list) > 0:
                for idx in order_list:
                    combis += combination(orders[idx], count)
        if len(combis) > 0:
            cnt = Counter(combis).most_common()
            # 최빈값을 후보로 등록
            maximum = cnt[0][1]
            if maximum >= 2:
                for c in cnt:
                    if c[1] == maximum:
                        answer.append(c[0])
                    else:
                        break

    answer.sort()

    return answer


def combination(arr, r) -> list:

    combi = []

    def generate(chosen):
        if len(chosen) == r:
            combi.append(''.join(sorted(chosen)))
            return

        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            chosen.append(arr[nxt])
            generate(chosen)
            chosen.pop()
    generate([])
    return combi


# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
# print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))


# 다른 사람의 풀이. 조합 라이브러리 사용.
def solution_another(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        result += [k for k, v in most_ordered
                   if v > 1 and v == most_ordered[0][1]]

    return [''.join(v) for v in sorted(result)]

