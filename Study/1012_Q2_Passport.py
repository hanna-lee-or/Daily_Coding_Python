# 백준 3079 / 입국심사 (이분탐색)
# 입국심사대 N개, 친구 M명, 심사시간 Tk
# 심사를 마치는데 걸리는 최솟값

import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
time = []
# 심사시간 입력 받기
end = 0
for i in range(n):
    t = int(sys.stdin.readline().rstrip())
    time.append(t)
    if t > end:
        end = t

start = 0
end = end * m
answer = 0
while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in range(n):
        count += mid // time[i]
    if count >= m:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)



