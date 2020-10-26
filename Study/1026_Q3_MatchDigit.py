# 백준 3687 / 성냥개비
# 미완. 좀 더 고민해보기!!

# 십진수를 성냥개비로 표현할 때
# 주어진 성냥으로 만들 수 있는 수 중
# 최소와 최대 구하기

import sys


match = dict()
match[2] = ["1"]
match[3] = ["7"]
match[4] = ["4"]
match[5] = ["2", "3", "5"]
match[6] = ["0", "6", "9"]
match[7] = ["8"]

# 10 이하의 답 미리 구해놓기
# n=0일때 -> 이미 최솟값으로 완성된 상태이다. (8888....)
# n=1일때 -> 앞에 8을 하나 지우고 10을 붙이면 된다.
# n=2일때 -> 앞에 1만 붙이면 된다
ans = [0, 0, 1, 7, 4, 2, 6, 8, 10, 18, 22]


# 최대값 만드는 함수
def make_maxi(count):
    div, mod = divmod(count, 2)

    s = '7' * mod + '1' * (div-1)

    return s


# 최소값 만드는 함수
def make_mini(count):
    div, mod = divmod(count, 7)
    s = "-1"

    if mod == 0:
        for i in range(div):
            s += match[7][0]
    # div + 1 : 숫자 자리 수
    else:
        pass

    return s


# 테스트 케이스 개수
t = int(sys.stdin.readline().rstrip())

mini_list = []
maxi_list = []
for _ in range(t):
    count = int(sys.stdin.readline().rstrip())
    # mini는 자리수를 줄이는게 일단 핵심
    mini = "-1"

    if count <= 10:
        mini = str(ans[count])
    else:
        ansMin = ''
        while count > 0:
            count -= 7
            if count >= 0:
                ansMin += '8'
            else:
                count += 7; break

        small = {6: 6, 2: 1, 5: 2}
        if count in small:
            ansMin = str(small[count]) + ansMin
        else:
            if count == 1:
                ansMin = '10' + ansMin[1:]
            elif count == 3:
                ansMin = '200' + ansMin[2:]
            elif count == 4:
                ansMin = '20' + ansMin[1:]
        mini = ansMin

    mini_list.append(mini)
    maxi_list.append(make_maxi(count))

for i in range(t):
    print(mini_list[i], maxi_list[i])
