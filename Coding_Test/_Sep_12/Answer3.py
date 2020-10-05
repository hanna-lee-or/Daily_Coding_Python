#카카오 코딩 테스트 3번


def solution(info, query):

    N = len(info)
    dataSheet = []
    # 데이터 저장
    for i in range(N):
        list = info[i].split()
        dataSheet.append(list)
        print(list)

    Qn = len(query)
    answerSheet = [0] * Qn
    # 데이터 검색
    for i in range(Qn):
        temp = query[i].replace('and', '')
        temp = temp.split()
        print(i, '=>', temp)

        count = 0
        dataFlag = [True] * N
        # 한 사람씩 체크
        for one in range(N):
            # 점수 데이터 확인
            if (int(temp[4]) > int(dataSheet[one][4])):
                dataFlag[one] = False
                continue
            #info 확인
            for k in range(4):
                if(temp[k] == '-'):
                    continue
                elif(temp[k] != dataSheet[one][k]):
                    dataFlag[one] = False
                    print(one, ',', k, ':', temp[k], dataSheet[one][k])
                    break

            #적합한 데이터인지 확인
            if (dataFlag[one] == True):
                count += 1

        answerSheet[i] = count

    return answerSheet

print(solution(["java backend junior pizza 150", "python frontend senior chicken 210",
                "python frontend senior chicken 150", "cpp backend senior pizza 260",
                "java backend junior chicken 80","python backend senior chicken 50"],
               ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
                "cpp and - and senior and pizza 250", "- and backend and senior and - 150",
                "- and - and - and chicken 100", "- and - and - and - 150"]))

