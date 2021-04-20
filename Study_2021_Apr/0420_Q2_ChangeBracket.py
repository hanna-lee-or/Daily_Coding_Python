# 프로그래머스 Level2 괄호 변환
# 잘못된 괄호를 특정 기준에 따라 변환하기
# 문제 이해하기 => 균형잡힌 (개수가 같은), 올바른(짝이 맞는)

"""
1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
   단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며,
   v는 빈 문자열이 될 수 있습니다.
   ('('의 개수와 ')'의 개수가 같으면 균형잡힌 괄호 문자열이라고 부릅니다.)

3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.

4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
  4-3. ')'를 다시 붙입니다.
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
  4-5. 생성된 문자열을 반환합니다.
"""


#
def solution(p):

    # 1단계. 입력이 빈 문자열인 경우, 빈 문자열 반환.
    if p == '':
        return ''
    else:
        # 2단계. u, v로 문자열 분리하기.
        stack = []
        flag = True
        balance = 0
        i = 1
        for c in p:
            if c == '(':
                balance -= 1
                if flag:
                    stack.append(0)
            else:
                balance += 1
                if flag:
                    if stack:
                        if stack[-1] == 0:
                            stack.pop()
                    else:
                        flag = False

            # 균형이 맞은 곳까지가 u, 나머지가 v
            if balance == 0:
                break
            else:
                i += 1

        if stack:
            flag = False

        u = p[:i]
        v = p[i:]
        print(f'u: {u}, v: {v} [{i}]')

        # 3단계. u가 올바르면 v 대상으로 1단계로 진입.
        if flag:
            return u + solution(v)
        else:
            # 4단계. u가 올바르지 않은 경우.
            u = u[1:]
            u = u[:-1]
            ru = ''
            for c in u:
                if c == '(':
                    ru += ')'
                else:
                    ru += '('

            return '(' + solution(v) + ')' + ru


print(solution("()))((()"))


# 다른 사람의 풀이. 람다 함수 활용.
def solution_another(p):

    if p == '':
        return p

    r = True
    c = 0
    for i in range(len(p)):
        if p[i] == '(':
            c -= 1
        else:
            c += 1

        if c > 0:
            r = False
        if c == 0:
            if r:
                return p[:i+1]+solution(p[i+1:])
            else:
                return '('+solution(p[i+1:])+')'+''\
                    .join(list(map(lambda x: '(' if x == ')' else ')', p[1:i])))
