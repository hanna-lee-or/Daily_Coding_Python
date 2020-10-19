# 프로그래머스 월간 코드 챌린지 쿼드압축 후 개수 세기
# Hanna 2020/10/19

#



def solution(arr):

    count = len(arr)
    dx = [0, 0, 1, 1]
    dy = [0, 1, 0, 1]
    while count > 1:
        zip = []
        for i in range(0, count, 2):
            row_zip = []
            for j in range(0, count, 2):
                # print(i, j)
                mark = arr[i][j]
                flag = True
                nemo = []
                for k in range(4):
                    m = arr[i + dx[k]][j + dy[k]]
                    if isinstance(m, list):
                        s = ""
                        for c in m:
                            s += str(c)
                        nemo.append(s)
                        flag = False
                        continue
                    elif m != mark:
                        flag = False
                    nemo.append(m)
                if flag:
                    row_zip.append(mark)
                else:
                    row_zip.append(nemo)
            zip.append(row_zip)
        count = count // 2
        arr = zip
    print(arr)

    count = [0, 0]
    for mtx in arr:
        if isinstance(mtx, int):
            count[mtx] += 1
            break
        for m in mtx:
            for s in m:
                if isinstance(s, int):
                    count[s] += 1
                else:
                    for c in s:
                        if c == '1':
                            count[1] +=1
                        else:
                            count[0] += 1

    return count


print('\nanswer :', solution([1]))
