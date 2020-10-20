# 프로그래머스 월간 코드 챌린지 쿼드압축 후 개수 세기
# Hanna 2020/10/21

# isinstance(변수, 타입) : 변수가 타입에 해당하는지 체크
# 해당 문법 기억하기!


import numpy as np


# 다른 사람의 답 (numpy 및 재귀함수 이용)
def solution_another(arr):
    # 재귀함수 구현
    def fn(a):
        # 원소가 모두 0이면
        if np.all(a == 0):
            return np.array([1, 0])
        # 원소가 모두 1이면
        if np.all(a == 1):
            return np.array([0, 1])
        # 아니라면 재귀함수를 통한 분할 정복
        n = a.shape[0]//2
        return fn(a[:n, :n]) + fn(a[n:, :n]) + fn(a[:n, n:]) + fn(a[n:, n:])

    # 결과 리턴
    return fn(np.array(arr)).tolist()


# 나의 답 (코드는 길지만, 재귀를 안쓴다는 것에 의의를...)
def solution(arr):

    count = len(arr)
    dx = [0, 0, 1, 1]
    dy = [0, 1, 0, 1]
    while count > 1:
        zip = []
        for i in range(0, count, 2):
            row_zip = []
            for j in range(0, count, 2):
                mark = -1
                flag = True
                nemo = [0, 0]
                for k in range(4):
                    m = arr[i + dx[k]][j + dy[k]]
                    if isinstance(m, list):
                        flag = False
                        nemo[0] += m[0]
                        nemo[1] += m[1]
                        continue
                    elif mark == -1:
                        mark = m
                    elif m != mark:
                        flag = False
                    # m이 숫자인 경우. 0/1 카운트.
                    if m == 1:
                        nemo[1] += 1
                    else:
                        nemo[0] += 1
                if flag:
                    row_zip.append(mark)
                else:
                    row_zip.append(nemo)
            zip.append(row_zip)
        count = count // 2
        arr = zip
        print(arr)

    while isinstance(arr[0], list):
        arr = arr[0]

    if len(arr) == 1:
        count = [0, 0]
        count[arr[0]] += 1
        arr = count

    return arr


print('\nanswer :', solution([[1, 1, 1, 1, 1, 1, 1, 1],
                              [0, 1, 1, 1, 1, 1, 1, 1],
                              [0, 0, 0, 0, 1, 1, 1, 1],
                              [0, 1, 0, 0, 1, 1, 1, 1],
                              [0, 0, 0, 0, 0, 0, 1, 1],
                              [0, 0, 0, 0, 0, 0, 0, 1],
                              [0, 0, 0, 0, 1, 0, 0, 1],
                              [0, 0, 0, 0, 1, 1, 1, 1]]))

# print('\nanswer :', solution([[1, 1, 0, 0],
#                               [1, 0, 0, 0],
#                               [1, 0, 0, 1],
#                               [1, 1, 1, 1]]))


# print('\nanswer :', solution([[1]]))
