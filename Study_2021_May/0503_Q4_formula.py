# 프로그래머스 Level2 수식 최대화
# 숫자들과 3가지의 연산문자(+, -, *) 만으로 이루어진 연산 수식
#  연산자의 우선순위를 새로 정의할 때, 절대값이 가장 큰 결과값

# expression은 길이가 3 이상 100 이하인 문자열입니다.


import re
from itertools import permutations


# 나의 답.
def solution(expression):

    op = ["+", "-", "*"]
    exp = []
    start = 0
    # 연산자와 피연산자 나누기
    for i, c in enumerate(expression):
        if c in op:
            exp.append(int(expression[start:i]))
            exp.append(c)
            start = i + 1
    exp.append(int(expression[start:]))
    print(exp)

    # 우선순위에 따라 계산하기
    def calculate(exp, op):

        print(f'{exp} // {op}')

        if len(exp) == 1:
            return abs(exp[0])

        answer = 0
        for o in ["+", "-", "*"]:
            if o not in op:
                i = 1
                next_exp = exp[:]
                while i < len(next_exp):
                    # 타겟 연산자인 경우 계산 진행
                    e = next_exp[i]
                    if e == o:
                        a = next_exp[i-1]
                        b = next_exp[i+1]
                        if e == '+':
                            next_exp[i-1:i+2] = [a+b]
                        elif e == '-':
                            next_exp[i-1:i+2] = [a-b]
                        elif e == '*':
                            next_exp[i-1:i+2] = [a*b]
                    # 아닌 경우 계산 진행 X
                    else:
                        i += 2
                answer = max(answer, calculate(next_exp, op + [o]))
        return answer

    return calculate(exp, [])


print(solution("100-200*300-500+20"))  # 60420
# print(solution("50*6-3*2"))  # 300


# 다른 사람의 답. 정규식 + eval 함수 사용.
# eval 함수는 매개변수로 받은 expression(=식)을 문자열로 받아서 실행하는 함수.
# eval("1+2") 라는 문자열이 매개변수로 들어오면
# 출력 값으로 3이라는 값을 반환하는 구조이다.
def solution_another(expression):
    #1
    op = [x for x in ['*', '+', '-'] if x in expression]
    op = [list(y) for y in permutations(op)]
    ex = re.split(r'(\D)', expression)

    #2
    a = []
    for x in op:
        _ex = ex[:]
        for y in x:
            while y in _ex:
                tmp = _ex.index(y)
                _ex[tmp-1] = str(eval(_ex[tmp-1]+_ex[tmp]+_ex[tmp+1]))
                _ex = _ex[:tmp]+_ex[tmp+2:]
        a.append(_ex[-1])

    #3
    return max(abs(int(x)) for x in a)


# 다른 사람의 답. 우선순위가 낮은 연산자를 기준으로 문자열 split 해나간다음
# eval 로 계산해 나가는 구조.
def solution_other(expression):
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answer = []
    for op in operations:
        a = op[0]
        b = op[1]
        temp_list = []
        for e in expression.split(a):
            temp = [f"({i})" for i in e.split(b)]
            temp_list.append(f'({b.join(temp)})')
        answer.append(abs(eval(a.join(temp_list))))
    return max(answer)
