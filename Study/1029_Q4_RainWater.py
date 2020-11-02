# leetcode 42 Trapping Rain Water
# 빗물의 양 구하기


# 코딩 테스트에서 많이 본 유형


class Solution:

    def trap(self, height) -> int:

        if len(height) <= 2:
            return 0

        area = 0
        left, right = 0, len(height) - 1
        left_h = height[left]
        right_h = height[right]
        # 높이가 가장 높은 곳으로 left, right가 귀결됨.
        while left < right:
            print(f'{left} > {area} < {right}')
            # 오른쪽이 더 높으면, 왼쪽 이동
            if left_h <= right_h:
                for nxt in range(left + 1, right + 1):
                    nxt_h = height[nxt]

                    if left_h <= nxt_h:
                        left = nxt
                        left_h = nxt_h
                        break

                    area += left_h - nxt_h

                if left == right:
                    break

            # 왼쪽이 더 높으면, 오른쪽 이동
            else:
                for nxt in range(right - 1, left - 1, -1):
                    nxt_h = height[nxt]

                    if right_h <= nxt_h:
                        right = nxt
                        right_h = nxt_h
                        break

                    area += right_h - nxt_h

                if right == left:
                    break

        return area


print(Solution().trap([0, 1, 0, 2, 1, 0,
                       1, 3, 2, 1, 2, 1]))


