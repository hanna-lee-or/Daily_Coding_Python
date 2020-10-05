# SW Expert Academy 파핑파핑 지뢰찾기
# 최소 몇 번의 클릭을 해야 지뢰가 없는 모든 칸에 숫자 표시?

T = int(input())
result = []
for test_case in range(1, T + 1):
    # 지뢰 찾기 표 크기 n * n
    n = int(input())

    map = []
    # 지뢰 * 지뢰X . 클릭한 지뢰가 없는 칸 c
    for k in range(n):
        info = input()
        temp = []
        for l in range(n):
            temp.append(info[l])
        map.append(temp)

    # target 주변 정찰하기 (정찰을 다 해놓을까?)
    def find_num(target):
        i, j = target
        if map[i][j] == '*':
            return -1
        count_map = 0
        count_pang = 0
        for a in range(-1, 2):
            for b in range(-1, 2):
                if a == 0 and b == 0:
                    continue
                if 0 <= i+a < n and 0 <= j+b < n:
                    count_map += 1
                    if map[i+a][j+b] == '*':
                        count_pang += 1
        # 인접 맵 숫자와 지뢰 숫자 리턴 (ex. 모서리는 인접 맵 3개)
        return count_pang

    # answer_sheet 참고하며 클릭 결과 진행
    def click(target):
        i, j = target
        # 클릭 가능한 지역이 아닌 경우 (지뢰 or 이미 클릭 된 곳)
        if map[i][j] != '.':
            return 0
        # 클릭 가능한데 주변에 지뢰가 있을 경우
        elif answer_sheet[i][j] != 0:
            map[i][j] = answer_sheet[i][j]
            return 1
        # 클릭도 가능하고 주변에 지뢰가 없을 경우 (연쇄작용 필요)
        map[i][j] = 0
        for a in range(-1, 2):
            for b in range(-1, 2):
                if a == 0 and b == 0:
                    continue
                if 0 <= i+a < n and 0 <= j+b < n:
                    click([i+a, j+b])
        return 1

    answer_sheet = [[0] * n for _ in range(n)]
    zero_q = []
    # 정찰을 통해 모든 맵 숫자 정보 기록해놓기
    for i in range(n):
        for j in range(n):
            answer = find_num([i, j])
            # 지뢰 칸은 -1 기록됨.
            answer_sheet[i][j] = answer
            if answer == 0:
                zero_q.append([i, j])

    # 정찰 -> 지뢰 숫자 0인 거 찾기 -> 클릭하기 (연쇄작용 구현)
    count = 0
    while zero_q:
        target = zero_q.pop()
        if map[target[0]][target[1]] == '.':
            count += click(target)

    for i in range(n):
        for j in range(n):
            if map[i][j] == '.':
                count += 1

    result.append("#" + str(test_case) + " " + str(count))

for r in result:
    print(r)



