# 백준 2304 / 창고 다각형

"""
7
2 4
11 4
15 8
4 6
5 3
8 10
13 6

Answer : 98
"""


import sys


n = int(sys.stdin.readline().rstrip())

height = dict()

# 높이 정보 입력받기
for _ in range(n):
    idx, h = map(int, sys.stdin.readline().rstrip().split())
    height[idx] = h

# 위치 정보 정렬하기
pos = list(height.keys())
pos.sort()
print(pos)
print(height)


area = 0
left, right = 0, n-1
left_h = height[pos[left]]
right_h = height[pos[right]]
# 높이가 가장 높은 곳으로 left, right가 귀결됨.
while left < right:
    print(f'{left} > {area} < {right}')
    # 오른쪽이 더 높으면, 왼쪽 이동
    if left_h <= right_h:
        i = left
        i_h = left_h
        for nxt in range(left+1, right+1):
            nxt_h = height[pos[nxt]]
            if left_h <= nxt_h:
                i = nxt
                i_h = nxt_h
                break
        if i == right:
            area += (pos[i] - pos[left])\
                    * min(left_h, right_h)
            left = i
            break
        else:
            area += (pos[i] - pos[left]) * left_h
        left = i
        left_h = height[pos[left]]
    # 왼쪽이 더 높으면, 오른쪽 이동
    else:
        i = right
        for nxt in range(right-1, left-1, -1):
            nxt_h = height[pos[nxt]]
            if right_h <= nxt_h:
                i = nxt
                i_h = nxt_h
                break
        if i == left:
            area += (pos[right] - pos[i])\
                    * min(left_h, right_h)
            right = i
            break
        else:
            area += (pos[right] - pos[i]) * right_h
        right = i
        right_h = height[pos[i]]


print(f'{left} > {area} < {right}')
print(area + height[pos[left]])





