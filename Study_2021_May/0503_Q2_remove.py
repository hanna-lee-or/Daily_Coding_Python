# 프로그래머스 Level2 짝지어 제거하기
# 같은 알파벳이 2개 붙어 있으면 제거 후 양 옆 이어붙임.
# 문자열이 모두 제거되면 1 반환. 아니면 0 반환.


# 나의 답. 스택 활용.
def solution(s):

    stack = []

    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    if stack:
        return 0
    else:
        return 1


print(solution("baabaa"))  # 1
print(solution("cdcd"))  # 0


