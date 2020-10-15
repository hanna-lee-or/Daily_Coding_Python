# 백준 1695 / 팰린드롬 만들기
# 수열에 최소 개수의 수를 끼워 넣어 팰린드롬을 만들려고 한다.
# 최소 몇 개의 수를 끼워 넣으면 되는가.

import sys

# 수열 길이 n, 수열 numbers
n = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
cache = [[-1] * n for _ in range(n)]


def palindrome(start, end):

    if start >= end:
        return 0

    count = cache[start][end]
    if count != -1:
        return count

    if numbers[start] == numbers[end]:
        count = palindrome(start+1, end-1)
    else:
        count = 1 + min(palindrome(start+1, end), palindrome(start, end-1))

    cache[start][end] = count
    return count


print(palindrome(0, n-1))
