# leetcode Container With Most Water
# 가장 물을 많이 채울 수 있는 구간 찾기
# 물의 최대 양 구하기

# 답지 참고. 투 포인터 사용 O(n).


from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        n = len(height)
        start, end = 0, n - 1

        maximum = 0
        while start < end:
            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1
            maximum = max(maximum, (end - start)*min(height[start], height[end]))

        return maximum


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))


