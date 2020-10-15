# 백준 9935 / 문자열 폭발
# 시간 초과 (미완)

import sys

# 문자열 s, 폭발 문자열 bomb
s = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()
bn = len(bomb)

i = 0
while i < len(s):
    if s[i] == bomb[0]:
        if s[i:i+bn] == bomb:
            s = s[:i] + s[i+bn:]
            i = i - bn
            if i <= 0:
                i = -1
    i += 1

if len(s) == 0:
    print("FRULA")
else:
    print(s)
