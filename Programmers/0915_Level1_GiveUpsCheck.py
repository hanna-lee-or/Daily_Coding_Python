# 프로그래머스 완전탐색 Level 1 모의고사
# 정답 많이 맞춘 수포자 알아내기
# Hanna 2020/09/15


# <파이썬 문법 메모>
# cycle(리스트) => 리스트 무한 반복
# answer_sheet = [cycle([리스트1]), cycle([리스트2]) ...]
# enumerate(리스트) => i 와 answer[i]를 튜플형태로 전달
# for idx, answer in enumerate(answers):


def solution(answers):
    answer = []

    answer_sheet = [[1, 2, 3, 4, 5],
                    [2, 1, 2, 3, 2, 4, 2, 5],
                    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    pattern = []
    for i in range(len(answer_sheet)):
        pattern.append(len(answer_sheet[i]))

    count = [0] * 3

    for i in range(len(answers)):
        for j in range(3):
            k = i % pattern[j]
            if answer_sheet[j][k] == answers[i]:
                count[j] += 1

    best = max(count)
    for i in range(3):
        if count[i] == best:
            answer.append(i+1)

    return answer


print(solution([1, 2, 3, 4, 5]))

