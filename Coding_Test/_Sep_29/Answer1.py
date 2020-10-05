# 11번가 코딩테스트 1
# Hanna 2020/09/29

# 메모


# 삽입가능한 a 개수 구하기
def solution(S):

    flag = 0
    count_a = 0
    S += "Z"

    for c in S:
        if c == 'a':
            flag += 1
        else:
            count_a += 2 - flag
            flag = 0
        if flag >= 3:
            count_a = -1
            break


    return count_a


print('\nanswer :', solution("aaa"))

