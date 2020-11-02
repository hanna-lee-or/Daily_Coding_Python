# 백준 1662 / 압축

# K(Q) : Q라는 문자열이 K번 반복
# dp 인 것 같음 ㅠ.ㅠ 머리 아프다

# 3(3(3(2(2)2(2))))
# 답은 180 이어야 함


import sys


s = sys.stdin.readline().rstrip()


# 미완성 코드
# 재귀를 사용하긴 해야함.
# 근데...머리아파서 일단 Pass...ㅎㅎ
def un_pack(Q):

    stack = []
    length = 0
    i = 0
    while i < len(Q):
        # 인덱스 저장
        if Q[i] == "(":
            stack.append(i)
        elif Q[i] == ")":
            start = stack.pop() - 1
            # 괄호 안 길이 더하고
            length += (i - start - 2)
            # K에 해당하는 수만큼 곱하기
            length *= int(Q[start])
            # 처리한 부분은 제거
            Q = Q[:start] + Q[i+1:]
            # i 이동
            i = start - 1
            # print(Q, length)
        i += 1

    return len(Q) + length


print(un_pack(s))

