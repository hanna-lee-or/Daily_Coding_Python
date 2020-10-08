# 백준 2003 / 수들의 합 2
# a, b 구간의 수들의 합이 m이 되는 경우의 수
# 시간초과 관리!!

import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

num = list(map(int, sys.stdin.readline().rstrip().split()))

count = 0
i = 0
j = 0

sum = 0
# 일단 합이 m이 되거나 넘는 구간 파악하기
for k in range(n):
    sum += num[k]
    if sum == m:
        j = k
        count += 1
        break
    elif sum > m:
        j = k
        break

# 모든 수를 더했을 때 m이거나 m이 되지 않는 경우
if j == n - 1 and sum <= m:
    print(count)
else:
    while i < n and j < n:
        # i를 오른쪽으로 이동하며 체크
        for k in range(i, j + 1):
            sum -= num[k]
            if sum == m:
                i = k + 1
                count += 1
                break
            elif sum < m:
                i = k + 1
                break
        if i >= n:
            break
        if i >= j:
            j = i
            sum = num[i]
        # j를 오른쪽으로 이동하며 체크
        for k in range(j+1, n):
            sum += num[k]
            if sum == m:
                j = k
                count += 1
                break
            elif sum > m:
                j = k
                break
        if j == n - 1 and sum <= m:
            break
    print(count)

"""
for a in range(n):
    sum = 0
    for b in range(a, n):
        sum += num[b]
        if sum == m:
            count += 1
            break
        elif sum > m:
            break
"""
