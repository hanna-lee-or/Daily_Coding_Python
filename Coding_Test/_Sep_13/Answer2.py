#라인 코딩 테스트 2번


def solution(ball, order):

    wait_list = []
    answer = []

    # 앞 뒤 확인
    def checkBall(ballA):
        if (ballA == ball[0]):
            answer.append(ballA)
            ball.pop(0)
        elif (ballA == ball[-1]):
            answer.append(ballA)
            ball.pop(-1)
        else:
            return False
        return True

    for i in range(len(order)):
        current_order = order[i]

        # 보류 상태 공 확인
        flag = True
        while flag == True:
            flag = False
            for j in range(len(wait_list)):
                if(checkBall(wait_list[j]) == True):
                    flag = True
                    wait_list.pop(j)
                    break

        # 앞 뒤 확인
        if(checkBall(current_order) == False):
            wait_list.append(current_order)

    print(wait_list)
    print(ball)

    j = 0
    while len(wait_list) > 0:

        if (j >= len(wait_list)):
            j = 0

        # 보류 상태 공 확인
        if (checkBall(wait_list[j]) == True):
            wait_list.pop(j)
        else:
            j += 1


    return answer


print(solution([11, 2, 9, 13, 24], [9, 2, 13, 24, 11]))
