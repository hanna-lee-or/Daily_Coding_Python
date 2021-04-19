# 프로그래머스 Level2 124 나라의 숫자
# 숫자 변환
# 124 나라에는 자연수만 존재한다.
# 124 나라에는 모든 수를 표현할 때 1, 2, 4만 사용한다.


# 정답 ㅎㅎ
def solution(n):
    answer = ""
    digit = [1, 2, 4]

    # 숫자 3개 => 3진법
    target = n
    while target > 0:
        target -= 1  # 124나라에는 0 처리가 없으므로 한 칸 조정해준다.
        target, b = divmod(target, 3)
        answer += str(digit[b])

    return answer[::-1]


print(solution(5))


# 다른 사람의 풀이, 재귀 활용
def solution_another(n):
    if n <= 3:
        return '124'[n-1]
    else:
        q, r = divmod(n-1, 3)
        return solution(q) + '124'[r]