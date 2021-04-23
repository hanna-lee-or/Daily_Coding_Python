# 프로그래머스 Level2 주식 가격
# 각각 가격이 떨어지지 않은 기간(초)


#
def solution(prices):
    answer = [0] * len(prices)

    for i in range(len(prices) - 1):
        for j in range(i, len(prices) - 1):
            if prices[i] > prices[j]:
                break
            else:
                answer[i] += 1

    return answer


# print(solution([1, 2, 3, 2, 3]))


# 다른 사람의 풀이. 속도 최적화.
def solution_another(p):

    ans = [0] * len(p)

    # 주식 가격이 처음으로 떨어지는 지점을
    # 아직 못찾은 가격의 Index 모음
    stack = [0]

    # stack 에 남은 것들이 i번 째에
    # 처음으로 가격이 떨어지는지 체크
    for i in range(1, len(p)):
        if p[i] < p[stack[-1]]:
            # stack 리스트를 역으로 도는 이유는
            # 내 뒤쪽 것이 p[i]보다 가격이 같거나 작으면
            # 그 앞의 것들은 i index 에서 최초로 가격이 떨어질리 없어
            # break 로 시간을 줄일 수 있기 때문.
            for j in stack[::-1]:
                if p[i] < p[j]:
                    ans[j] = i-j
                    stack.remove(j)
                    print(f'/ {j}({p[j]}) /')
                else:
                    break
        stack.append(i)
        print(f'{i}({p[i]}) ')
    
    # 끝까지 가격이 떨어지지 않은 것들
    for i in range(0, len(stack)-1):
        ans[stack[i]] = len(p) - stack[i] - 1

    return ans


print(solution_another([5, 2, 3, 2, 3]))
