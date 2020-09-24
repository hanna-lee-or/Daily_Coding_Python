# 프로그래머스 동적계획법(Dynamic) Level 3 정수 삼각형
# 아래로 내려가며 합산. 가장 큰 값은?
# Hanna 2020/09/24

# Dynamic Programming : 메모리를 약간 더 사용하여 연산 속도 증가
# 작은 문제에서의 답 -> 큰 문제로 확대


# 다른 사람의 답 1 (한 층씩 제거하며 이동거리를 두 번째 input으로...??)
solutionA = lambda t, l = []: max(l) if not t else solution(t[1:], [max(x,y)+z for x,y,z in zip([0]+l, l+[0], t[0])])


# 다른 사람의 답 2 (음! 체크리스트 안만들고 바로 다음층 값을 sum값으로!)
def solution(triangle):
    dp = []
    for t in range(1, len(triangle)):
        for i in range(t+1):
            if i == 0:
                triangle[t][0] += triangle[t-1][0]
            elif i == t:
                triangle[t][-1] += triangle[t-1][-1]
            else:
                triangle[t][i] += max(triangle[t-1][i-1], triangle[t-1][i])
    return max(triangle[-1])


# 나의 답
def solution(triangle):
    answer = 0

    check_list = []
    for i in range(len(triangle)):
        check_list.append([0] * len(triangle[i]))
    check_list[0][0] = triangle[0][0]

    def tri_sum(triangle, check_list):
        # 삼각형 층수만큼 반복 (마지막층 제외)
        for level in range(len(triangle)-1):
            for i in range(len(triangle[level])):
                sum = check_list[level][i]
                # 아래 두 경로의 합산 값 갱신
                check_list[level+1][i] = max(check_list[level+1][i], sum+triangle[level+1][i])
                check_list[level+1][i+1] = max(check_list[level+1][i+1], sum + triangle[level+1][i+1])

    tri_sum(triangle, check_list)
    # 마지막층 돌며 가장 큰 값 찾아내기
    for i in range(len(triangle[-1])):
        answer = max(answer, check_list[-1][i])

    return answer


print('\nanswer :', solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
