# 백준 1695 / 팰린드롬 만들기
# 수열에 최소 개수의 수를 끼워 넣어 팰린드롬을 만들려고 한다.
# 최소 몇 개의 수를 끼워 넣으면 되는가.
# left, right 끝이 다를 경우 무조건 right 추가 X
# left 추가함으로써 최소 개수로 팰린드롬 만들 수 있는 경우 있다는 거 유의

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

# 해당 문제는 C++로 풀어야 정답 처리 가능 (시간 효율성 관련)
"""
#include <iostream>
#include <cstdio>
using namespace std;

int n,dp[5002][5002], arr[5002];

int f(int l, int r)
{
    if(l>=r)
        return 0;
    int& ret = dp[l][r];
    if(ret!=0) return ret;

    if(arr[l]==arr[r])
    {
        ret = f(l+1, r-1);
        return ret;
    }
    ret = 1 + min(f(l,r-1), f(l+1,r));
    return ret;
}

int main()
{
    cin>>n;
    for(int i=0;i<n;i++)
        scanf("%d",&arr[i]);
    printf("%d\n",f(0,n-1));
    return 0;
}
"""
