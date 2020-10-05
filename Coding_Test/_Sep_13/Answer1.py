#라인 코딩 테스트 1번


def solution(boxes):

    check_list = [0] * 100000

    for i in range(len(boxes)):
        for j in range(2):
            check_list[boxes[i][j]] += 1

    count = 0
    for i in range(len(check_list)):
        if(check_list[i] > 0 & check_list[i]%2 == 0):
            count += check_list[i] // 2

    return len(boxes) - count


print(solution([[1, 2], [2, 3], [3, 1]]))


