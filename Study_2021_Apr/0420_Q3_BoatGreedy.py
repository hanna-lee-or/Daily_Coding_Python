# 프로그래머스 Level2 구명 보트
# 필요한 구명보트 최소 개수


# 정답
def solution(people, limit):

    people.sort(reverse=True)
    print(people)
    boat = 1

    i = 0
    j = len(people) - 1
    w = people[i]

    while i < j:
        w += people[j]
        if w > limit:
            i += 1
            w = people[i]
            boat += 1
        else:
            j -= 1

    return boat


print(solution([70, 50, 80, 50], 100))


# 다른 사람의 풀이. return len(people) - answer 이 포인트.
def solution_another(people, limit):
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b:
        if people[b] + people[a] <= limit:
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer
