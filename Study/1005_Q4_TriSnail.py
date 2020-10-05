# 프로그래머스 월간 코드 챌린지 1 삼각 달팽이
# 높이가 n인 삼각형에서 맨 위 꼭짓점부터 반시계 방향으로 달팽이 채우기를 진행
# 첫 행부터 마지막 행까지 모두 순서대로 합친 새로운 배열을 return

# 미완

def solution(n):

    answer = []

    triangle = []
    for i in range(1, n+1):
        temp = []
        for j in range(i):
            temp.append(0)
        triangle.append(temp)
    print(triangle)

    # 내려간다(+1, 0) > 오른쪽으로 간다(0, +1) > 올라간다(-1, -1) 반복
    number = 0
    x = 0
    y = -1
    for i in range(n):
        for j in range(n - i):
            number += 1
            type = i % 3
            if type == 0:
                y += 1
            elif type == 1:
                x += 1
            else:
                x -= 1
                y -= 1
            triangle[y][x] = number

    for floor in triangle:
        for k in floor:
            answer.append(k)

    return answer


print(solution(6))
