# 프로그래머스 찾아라 프로그래밍 Level 4 사칙연산
# Hanna 2020/10/16

# 뺄셈은 연산 순서에 따라 그 결과가 바뀔 수 있음.
# 서로 다른 연산순서의 계산 결과 중 최댓값을 return

# 어려우니까 나중으로...ㅎㅎ


def solution(arr):

    answer = 1

    for i in range(len(arr)):
        if i % 2 == 0:
            arr[i] = int(arr[i])

    return answer


print('\nanswer :', solution("1", "-", "3",
                             "+", "5", "-", "8"))
