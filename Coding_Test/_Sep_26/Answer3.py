# 네이버 코딩테스트 3
# Hanna 2020/09/26

# 메모

import math

def solution(k):

    # 성냥개비 i개로 만들 수 있는 숫자 count[i]개
    # 성냥개비 2~7개에서 숫자 만들 수 있음
    count = [0, 0, 1, 1, 1, 3, 3, 1]
    able = [2, 3, 4, 5, 6, 7]

    if k < 1:
        return 0

    answer = 0
    two = 0
    three = 0
    while True:
        # 2로만 쪼갰을 때
        two = k / 2
        b = k % 2
        if b == 0:
            answer += 1
        elif b == 1:
            flag2_1 = True
        else:
            continue
        # 3으로만 쪼갰을 때
        three = k / 3
        b = k % 3
        if b == 0:
            answer += 1
        elif b == 2:
            answer += three +1
            flag3_2 =True
        elif b == 1:
            flag3_1 = True

        # 2 and 4
        temp2 = two - 2
        temp4 = 1
        if temp2 == 0:
            answer += 1
        while temp2 > 0:
            answer += math.factorial(temp2+temp4)/math.factorial(temp4)
        
        # ㅠ.ㅠ

    return answer


print('\nanswer :', solution(5))