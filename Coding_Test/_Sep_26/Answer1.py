# 네이버 코딩테스트 1
# Hanna 2020/09/26

# 메모


# n은 날짜 수, p는 생산량, c는 주문량
# 일일 매출 평균 구하기 (return은 문자열로)
def solution(n, p, c):
    answer = ''

    price = 100
    day = n
    sum = 0
    for i in range(n):
        print("day", i, ":", p[i], "/", c[i])
        if price == 0:
            day = i
            break
        if p[i] >= c[i]:
            sum += c[i] * price
            if i < n - 1 and p[i] - c[i] > 0:
                p[i+1] += p[i] - c[i]
            print(i, "=>", sum)
            price = 100
        else:
            if i < n - 1:
                p[i+1] += p[i]
            if price == 100:
                price = 50
            elif price == 50:
                price = 25
            else:
                price = 0
    result = round(float(sum)/float(day), 2)
    print(sum, day, result)
    answer = str(result)
    flag = 0
    for s in range(len(answer)):
        if answer[s] == '.':
            flag += s+1
    if len(answer)-flag != 2:
        answer += '0'

    return answer


print('\nanswer :', solution(6, [5, 4, 7, 2, 0, 6], [4, 6, 4, 9, 2, 3]))