# 프로그래머스 연습문제 Level 3 가장 긴 팰린드롬
# 앞뒤를 뒤집어도 똑같은 문자열, 팰린드롬.
# 가장 긴 팰린드롬의 길이 구하기
# Hanna 2020/09/17


# 처음에 예외 경우*(문자열 길이가 0, 1인 경우)와
# 예외가 아닌 경우에도 답이 1이상임을 생각 못해서 틀림
# 경우를 꼼꼼히 생각하자!


# 다른 사람의 짧고 굵은 답 - Awesome
# (재귀 함수, 양 끝단을 잘라가며 뒤집어도 같은지 체크)
def longest_palindrom(s):
    return len(s) if s[::-1] == s else max(longest_palindrom(s[:-1]), longest_palindrom(s[1:]))


# 나의 답 (기준점 설정 후, 양옆 체크)
def solution(s):
    s_len = len(s)

    # 예외 경우
    if s_len == 0:
        return 0
    elif s_len == 1:
        return 1

    def check_palindrom(idx_mid, is_double):
        if not is_double:
            idx_left = idx_mid
            count = 1
        else:
            idx_left = idx_mid - 1
            count = 2
        idx_right = idx_mid
        # 중심 기준으로 양 옆 체크
        while idx_left > 0 and idx_right < s_len-1:
            idx_left -= 1
            idx_right += 1
            if s[idx_left] != s[idx_right]:
                return count
            else:
                count += 2
        return count

    # 문자열 길이가 2이상인 경우, 답은 1이상임.
    answer = 1
    for i in range(1, s_len-1):
        left, mid, right = s[i-1:i+2]
        # aba 경우, b 기준으로 양 옆 체크
        if left == right:
            answer = max(answer, check_palindrom(i, False))
        # aab 경우, aa 기준으로 양 옆 체크
        if left == mid:
            answer = max(answer, check_palindrom(i, True))

    return answer


print('\nanswer :', solution("abcddcba"))

print('\nanswer(Another) :', longest_palindrom("abcddcba"))
