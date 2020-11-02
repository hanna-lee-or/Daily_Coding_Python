# leetcode Longest Valid Parentheses
# 유효한 괄호 쌍의 최대 길이 값 구하기


# 스택 이용! 공간 복잡도 O(n), 시간 복잡도 O(n)


class Solution:

    def longestValidParentheses(self, s: str) -> int:

        stack = [-1]
        count = 0

        for i, c in enumerate(s):
            print(f'"{c}" >> {stack} /+{count}')
            # "("일 시, 스택에 인덱스 저장
            if c == "(":
                stack.append(i)
            # ")"일 시, count 처리 작업 진행
            else:
                # 시작 괄호 인덱스 제거
                if stack:
                    stack.pop()

                # 길이 체크, 최대 길이 저장
                if stack:
                    count = max(count, i - stack[- 1])
                # 다음 유효 괄호를 체크하기 위해
                # 현재 인덱스 스택에 저장
                else:
                    stack.append(i)
        print(f'" " >> {stack} /+{count}')

        return count


print(Solution().longestValidParentheses("()(()"))


