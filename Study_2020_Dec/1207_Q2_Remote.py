# 백준 1107 / 리모컨
# 이동하고자 하는 채널로 가고자 한다면
# 최소 버튼을 몇 번 눌러야 하는가
# 현재 채널은 100
# 고장난 버튼 존재

"""
500000
8
0 2 3 4 6 7 8 9

Answer : 11117
"""

import sys

# target : 타켓 넘버
# n : 고장난 버튼의 갯수
# broke : 고장난 버튼
# check[i] : i번 버튼이 고장났는 지 여부
target = int(sys.stdin.readline())
n = int(sys.stdin.readline())
broke = list(map(int, sys.stdin.readline().split()))
check = [True] * 10

ans = 9876543210

# 고장난 버튼 반영
for i in broke:
    check[i] = False


# can_make : a를 현재 남아있는 버튼으로
# 갈 수 있는지 없는지 리턴하는 함수
def can_make(a):
    for k in str(a):
        if not check[int(k)]:
            return False
    return True


# 문제의 최소값은 0부터 최대값 999,906(1,000,000으로 대체)에
# 반드시 있으므로 탐색
for i in range(1000001):
    # 만일 해당 수에 도달할 수 있으면(평균적 경우)
    if can_make(i):
        # 최소값 갱신
        ans = min(ans, len(str(i)) + abs(i - target))
# 최악의 경우(애초에 10개 모두 고장나거나, 도달할 수 없다면)는
# 항상 100과의 비교가 유일하므로 최소값 갱신
ans = min(ans, abs(100 - target))

# 정답 출력
print(ans)


"""
# 틀린답
import bisect
import sys


dest = int(sys.stdin.readline())
bn = int(sys.stdin.readline())
if bn == 0:
    print(min(len(str(dest)), abs(100 - dest)))
elif bn == 10:
    break_b = set(map(int, sys.stdin.readline().split()))
    print(abs(100 - dest))
else:
    break_b = set(map(int, sys.stdin.readline().split()))
    able_b = []
    near_b = dict()
    for i in range(10):
        if i not in break_b:
            able_b.append(i)
            near_b[str(i)] = str(i)
    an = len(able_b)

    for b in break_b:
        idx = bisect.bisect_left(able_b, b)
        if idx == 0:
            near_b[str(b)] = str(able_b[0])
        elif idx == an:
            near_b[str(b)] = str(able_b[-1])
        else:
            left, right = able_b[idx-1], able_b[idx]
            if abs(left - b) < abs(right - b):
                near_b[str(b)] = str(left)
            else:
                near_b[str(b)] = str(right)

    end_s = str(dest)
    start_s = ""
    count = 0
    flag = False
    for c in end_s:
        if not flag:
            if near_b[c] != 0:
                flag = True
                start_s += near_b[c]
                count += 1
        else:
            start_s += near_b[c]
            count += 1

    count += abs(dest - int(start_s))
    if abs(dest - 100) < count:
        count = abs(dest - 100)
    print(f'dest: {end_s}, start: {start_s}')
    print(f'count: {count}')
"""
