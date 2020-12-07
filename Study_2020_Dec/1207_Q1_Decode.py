# leetcode 394 Decode String
# 문자열 디코딩하기

# 조금은 빨리 푸는 연습도 해보자
# 스스로 풀기 (Runtime 36ms)
class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        nums = []
        i = 0
        while i < len(s):
            c = s[i]
            # 반복 숫자 체크, '[' 체크
            if c.isdigit():
                start_i = i
                while s[i] != '[':
                    i += 1
                nums.append([start_i, int(s[start_i:i])])
                stack.append(i+1)
            # 디코딩
            elif c == ']':
                start_i, rep = nums.pop()
                start_s = stack.pop()
                if i == len(s) - 1:
                    s = s[:start_i] + s[start_s:i] * rep
                    break
                else:
                    temp = s[i + 1:]
                    s = s[:start_i] + s[start_s:i] * rep
                    i = len(s)
                    s += temp
            else:
                i += 1

        return s


print(Solution().decodeString("3[a2[c]]"))
