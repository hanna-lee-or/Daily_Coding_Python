# LeetCode 322 동전 교환 (DP문제)
# Hanna 2020/10/22

# amount에 도달할 수 있는 동전 개수의 최소값

from typing import List


# 답지 참고. 이해... 노력...
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        coins.sort(reverse=True)

        rs = [amount+1] * (amount + 1)
        rs[0] = 0
        # 아래에서 위로 타고 올라가며 최솟값 갱신
        for i in range(1, amount+1):
            for c in coins:
                if i >= c:
                    rs[i] = min(rs[i], rs[i-c] + 1)
                    print(i, "[", rs[i], "] -", c)

        # rs[i] 값이 amount + 1 값이면 경우의 수가 없는 것.
        if rs[amount] == amount + 1:
            return -1

        return rs[amount]


print(Solution().coinChange([1, 2, 5], 11))

