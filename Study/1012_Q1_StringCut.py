# 백준 2866 / 문자열 잘라내기 (매개변수 탐색)
"""
6 6
qwerqy
asdbgh
zxcvbn
aceeda
abdbza
cbedqc

입력이 위와 같을 때,
답 => 2 (zxcvbn 행 기준으로 aac 중복)
"""

import sys

r, c = map(int, sys.stdin.readline().rstrip().split())
s = [""] * c
for i in range(r):
    string = sys.stdin.readline().rstrip()
    for j in range(c):
        s[j] += string[j]

start = 0
end = r
trace = False
answer = 0
while start <= end:
    check = set()
    middle = (start + end) // 2
    flag = False
    for i in range(c):
        sub_s = s[i][middle:]
        if sub_s in check:
            flag = True
            answer = middle
            break
        else:
            check.add(sub_s)
    if not flag:
        start = middle + 1
    else:
        end = middle - 1
    print(flag, start, middle, end)

print(answer-1)



