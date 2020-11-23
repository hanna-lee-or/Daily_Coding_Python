# leetcode 5 Longest Palindromic Substring
# 유효한 팰린드롬의 가장 긴 길이


# 구글에 있는 답안 (Runtime 132ms)
class Solution:

    def longestPalindrome(self, s: str) -> str:

        if len(s) <= 1:
            return s

        # 가장 긴 substring의 시작 index를 idx에, 길이는 ln에 저장한다.
        idx, ln = 0, 0
        # j를 기준(j가 오른쪽 끝)으로 ln+1만큼의 길이를 가진
        # substring이 팰린드롬인지 검사. 맞으면 idx와 ln을 update.
        for j in range(len(s)):
            if s[j - ln: j + 1] == s[j - ln: j + 1][::-1]:
                idx, ln = j - ln, ln + 1
                print(j, ": ", s[idx: idx+ln])
            elif j - ln > 0 and s[j - ln - 1: j + 1] == s[j - ln - 1: j + 1][::-1]:
                idx, ln = j - ln - 1, ln + 2
                print(j, ":: ", s[idx: idx+ln])

        return s[idx: idx + ln]


print(Solution().longestPalindrome("badaeakkaea"))


# 파이썬 알고리즘 인터뷰에 있는 답안 (Runtime 272ms)
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # 팰린드롬 판별 및 투 포인터 확장
        def expand(left: int, right: int) -> str:
            while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
                left -= 1
                right += 1
            return s[left + 1:right - 1]
        
        # 해당 사항이 없을 때 빠르게 리턴
        if len(s) < 2 or s == s[::-1]:
            return s
        
        result = ''
        # 슬라이딩 윈도우 우측으로 이동
        for i in range(len(s) - 1):
            result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)

        return result
"""

