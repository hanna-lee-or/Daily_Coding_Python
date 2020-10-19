# 백준 1992 / 쿼드 트리
# Hanna 2020/10/19

# 모든 숫자가 같은 경우에는 () 출력 X
# 이 점을 놓쳐서 100%에서 틀림.
# 100%에서 틀리면 항상 최대, 최소, 예외 케이스 생각하기!

import sys

# 영상의 크기 N
N = int(sys.stdin.readline().rstrip())


matrix = [[[0] for _ in range(N)] for _ in range(N)]
for i in range(N):
    row = sys.stdin.readline().rstrip()
    for j, r in enumerate(row):
        if r == '1':
            matrix[i][j][0] = 1

gap = 2
count = N
dx = [0, 0, 1, 1]
dy = [0, 1, 0, 1]
while count > 1:
    zip = []
    for i in range(0, count, 2):
        row_zip = []
        for j in range(0, count, 2):
            # print(i, j)
            mark = matrix[i][j][0]
            flag = True
            nemo = []
            for k in range(4):
                m = matrix[i + dx[k]][j + dy[k]]
                if len(m) != 1:
                    s = "("
                    for c in m:
                        s += str(c)
                    s += ")"
                    nemo.append(s)
                    flag = False
                    continue
                elif m[0] != mark:
                    flag = False
                nemo.append(m[0])
            if flag:
                row_zip.append([mark])
            else:
                row_zip.append(nemo)
        zip.append(row_zip)
    count = count // 2
    matrix = zip

answer = ""
for mtx in matrix:
    for m in mtx:
        for s in m:
            if isinstance(s, int):
                answer += str(s)
            else:
                answer += s

# 모든 숫자가 같은 경우에는 () 출력 X
if len(answer) == 1:
    print(answer)
else:
    print("("+answer+")")
