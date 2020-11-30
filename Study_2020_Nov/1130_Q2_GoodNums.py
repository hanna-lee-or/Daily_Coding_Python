# 백준 2661 / 좋은 수열 (백트래킹)
# 숫자 1, 2, 3으로만 이루어지는 수열
# 임의의 길이의 인접한 두 개의 부분 수열이 동일한 것이 있으면 나쁜 수열

# 첫 번째 줄에 1, 2, 3으로만 이루어져 있는 길이가 N인
# 좋은 수열들 중에서 가장 작은 수를 나타내는 수열만 출력

# 어려운 백트래킹... 답지 분석 중...

"""
7

Answer : 1213121
"""


from sys import exit


def solve(s, _len):
    for d in range(1, _len//2 + 1):
        a = int(s[_len-d:])
        b = int(s[_len-2*d:_len-d])
        if a == b:
            return

    if _len == n:
        print(int(s))
        exit()

    for i in ['1', '2', '3']:
        solve(s+i, _len+1)


n = int(input())
solve('1', 1)

