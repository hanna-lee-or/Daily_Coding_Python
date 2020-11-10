# leetcode 32 Longest Valid Parentheses
# 유효한 괄호쌍의 가장 긴 길이 (복습)


class Solution:

    def longestValidParentheses(self, s: str) -> int:

        stack = [-1]
        count = 0

        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                if stack:
                    stack.pop()

                if stack:
                    count = max(count, i - stack[-1])
                else:
                    stack.append(i)

        return count


# print(Solution().longestValidParentheses("(()"))
print(Solution().longestValidParentheses(")()())"))

