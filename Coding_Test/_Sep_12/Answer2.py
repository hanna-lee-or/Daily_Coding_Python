#카카오 코딩 테스트 2번
from itertools import combinations


def solution(orders, course):

    answer = []
    result = set()
    n = len(orders)

    for i in range(len(course)):
        customer = []
        # 주문자마다 조합을 구한다.
        for j in range(n):
            # 조합에 필요한 길이를 충족하는 경우에만
            if(len(orders[j]) >= course[i]):
                tempList = list(combinations(orders[j], course[i]))
                #print(i, ',', j, '=>', tempList)
                # 튜플형태의 조합들을 오름차순인 알파벳 문자열로 변경
                newList = [] * len(tempList)
                for k in range(len(tempList)):
                    charList = []
                    char = ''
                    for c in range(course[i]):
                        charList.append(tempList[k][c])
                    charList.sort()
                    for c in range(course[i]):
                        char += charList[c]
                    newList.append(char)
                    newList.sort()
                customer.append(set(newList))

        print(course[i], '=>', customer)
        for a in range(len(customer)):
            for c in range(a+1, len(customer)):
                print(a, '-', c, '=>', customer[a].intersection(customer[c]))
                result.update(customer[a].intersection(customer[c]))
    answer = list(result)
    answer.sort()
    return answer


print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))

