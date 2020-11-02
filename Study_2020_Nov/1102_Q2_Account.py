# 프로그래머스 Level 1 예산
# 최대 몇 개의 부서에 물품을 지원할 수 있는가


def solution(d: list, budget: int) -> int:

    d.sort()
    sum_d = 0
    count = 0
    n = len(d)
    while sum_d + d[count] <= budget:
        print(f'sum : {sum_d}, count: {count}')
        sum_d += d[count]
        count += 1
        if count == n:
            break

    return count


print(solution([1, 3, 2, 5, 4], 9))
print(solution([2, 2, 3, 3], 10))

