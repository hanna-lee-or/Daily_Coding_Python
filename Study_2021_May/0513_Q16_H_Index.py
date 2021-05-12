# 프로그래머스 Level2 H-Index
# H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다.
# 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다.
# 어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고
# 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index 입니다.

# 어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때,
# 이 과학자의 H-Index를 return 하라.

# 논문의 수는 1편 이상 1,000편 이하
# 논문별 인용 횟수는 0회 이상 10,000회 이하


# 참고 답안
def solution(citations):
    citations.sort()
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            # 논문이 인용된 횟수(h번 이상) >= 인용된 논문의 개수(h개 == h번)
            return l-i
    return 0


print(solution([3, 0, 6, 1, 5]))  # 3


# 다른 사람의 풀이
def solution_another(citations):
    citations.sort(reverse=True)
    print(citations)
    # enumerate에 start를 이용해서 현재 자신보다 큰 수가 몇개 있는지 판별
    # map 함수를 통해 h값들의 집합을 만든다. h값중 최대값(max) 이 답이 된다.
    answer = max(map(min, enumerate(citations, start=1)))
    for i, x in enumerate(citations, start=1):
        print(i, x)
    return answer


print(solution_another([3, 0, 6, 1, 5]))  # 3
