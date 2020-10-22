# LeetCode 22 괄호 생성 (DP)
# Hanna 2020/10/22

# n개의 쌍 괄호로 만들 수 있는 모든 조합 출력
# 1 <= n <= 8


from typing import List


# 나의 답! 정답 ㅎㅎ
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # n = 1 일 때
        # ()
        # n = 2 일 때
        # (()), ()()
        # n = 3 일 때
        # ((())), (()()), (())(), ()(()), ()()()
        dp = [set() for _ in range(n+1)]
        dp[1].add("()")
        for i in range(2, n+1):
            # 속에 넣는 경우
            for s in dp[i-1]:
                dp[i].add("(" + s + ")")
            # 둘로 나누는 경우
            for j in range(1, i):
                for a in dp[j]:
                    for b in dp[i-j]:
                        dp[i].add(a + b)

        return dp[n]


print(Solution().generateParenthesis(3))
