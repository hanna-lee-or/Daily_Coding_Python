# 프로그래머스 Level2 예상 대진표
# N 명이 참가하는 토너먼트에서 A 와 B가 몇 번째 라운드에서 만나게 되는지.
# A번 참가자와 B번 참가자는 서로 붙게 되기 전까지 항상 이긴다고 가정한다.

# N은 2의 1승 ~ 2의 20승 (2의 지수 승으로 주어진다.)
# A, B : N 이하인 자연수 (A != B)


# 나의 답. 순열 사용.
def solution(n, a, b):

    count = 0
    a -= 1
    b -= 1
    while n > 0:
        a = a//2
        b = b//2
        print(f"a({a}조), b({b}조), n({n})")
        count += 1
        if a == b:
            break
        n //= 2

    return count


# print(solution(8, 1, 7))  # 3


# 다른 사람의 풀이. 띠용...
def solution_another(n, a, b):
    print(bin(a-1))
    print(bin(b-1))
    print(bin((a-1)^(b-1)))
    return ((a-1)^(b-1)).bit_length()


print(solution_another(8, 1, 7))  # 3

# <댓글 분석>
# 토너먼트 트리를 그렸을 때, 윗단을 최상위 비트,
# 아래단을 최하위 비트로 생각하면 이해되실 것 같네요.
# 가령, 5(101)의 가장 앞의 비트값(최상위)가 트리의 꼭대기

# xor 취하는 과정에서 ab 사이의 거리가 가까우면 상위비트가 차이 나지 않음.
