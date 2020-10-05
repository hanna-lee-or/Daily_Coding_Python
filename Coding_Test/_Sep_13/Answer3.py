#라인 코딩 테스트 3번


def solution(n):
    answer = []
    temp_list = []
    count = 0
    while n >= 10:
        # 몫 연산으로 숫자 쪼개기
        length = len(str(n))
        for i in range(1, length):
            ten = 10**(length-i)
            a = n // ten
            b = n % ten
            if(len(str(a)) + len(str(b)) == length):
                temp_list.append(a+b)
        temp_list.sort()
        n = temp_list[0]
        print(n)
        count += 1

    answer = [count, n]

    return answer



print(solution(10007))


