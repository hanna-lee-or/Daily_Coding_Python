# 프로그래머스 Level2 큰 수 만들기
# K 개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자


# 나의 답. 테스트 10번 시간 초과.
def solution(number, k):

    start_idx = 0
    while k > 0:
        past = '9'
        end_flag = True
        for i, n in enumerate(number[start_idx:]):
            # 상승세를 보이면 이전 숫자를 제거한다.
            if past < n:
                idx = start_idx + i
                number = number[:idx-1] + number[idx:]
                k -= 1
                end_flag = False
                start_idx = max(0, idx-2)
                break
            past = n
        # number 전체가 하락세이면 끝 자리를 k만큼 제거한다.
        if end_flag:
            number = number[:-k]
            break

    return number


print(solution("1924", 2))  # 94
print(solution("1231234", 3))  # 3234
print(solution("4177252841", 4))  # 775841


# 다른 사람의 답. 스택 활용.
def solution_another(number, k):
    stack = [number[0]]
    for num in number[1:]:
        # 숫자를 읽어나가며 더 큰 수가 나올 경우 교환.
        while stack and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)
