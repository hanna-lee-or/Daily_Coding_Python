# 백준 16571 / 알파 틱택토
# 먼저 3개의 연속 된 O 또는 X를 완성시킨 플레이어가 승리하게 된다.
# 이 게임은 무승부가 가능하다.

# 지금까지 진행 된 틱택토 게임 보드가 주어졌을 때,
# 이번에 착수하는 플레이어가 얻을 수 있는 최선의 게임 결과는 무엇일까?
# 두 플레이어는 항상 모든 경우를 고려하여 최선의 수를 둔다고 가정

# 0은 빈칸, 1은 X, 2는 O를 의미. 항상 X가 선공.
# 이기는 경우 "W", 무승부인 경우 "D", 지는 경우 "L"을 출력한다.
# 이번에 착수하는 플레이가 얻을 수 있는 최선의 게임 결과 출력하기.

# 틀림. 일단 나중에 답지 보는 걸로...
# https://m.blog.naver.com/adamdoha/221911376782
# ㄴ 답지 코드 (java)


"""
1 2 0      ||  1 2 0
1 1 2      ||  0 1 0
0 0 2      ||  0 0 0
           ||
Answer :   ||  Answer:
W          ||  L
"""


import sys


# 3X3 보드판 입력 받기
arr = []
for _ in range(3):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

# 1, 2의 개수를 세어, 현재 플레이어를 알아냄.
count = [0, 0, 0]
# 비어있는 공간 체크
empty = []
for i in range(3):
    for j in range(3):
        k = arr[i][j]
        if k == 0:
            empty.append([i, j])
        count[k] += 1

# 현재 플레이어 설정
if count[1] == count[2]:
    player = 1
    enemy = 2
else:
    player = 2
    enemy = 1


# 상태 확인
def check_state(player: int, enemy: int, count_state: list):
    # 이기는 경우 (1순위)
    if count_state[player] == 3:
        return 1
    # 방어해야 되는 경우 (2순위)
    elif count_state[enemy] == 2:
        return 2
    # 공격 가능한 경우 (이 경우가 2 이상 쌓이면 무조건 이김)
    elif count_state[player] == 2 and count_state[0] == 1:
        return 3
    # 위 경우에 해당하지 않는 경우
    else:
        return 0


# 틱택토 플레이
def play(player: int, enemy: int, empty: list) -> str:
    count_state = [0, 0, 0]
    shield = []
    attack = [0]
    
    # 상태에 따른 동작 함수
    def do_state(state, ei, ej):
        if state == 1:
            return True
        elif state == 2:
            shield.append([ei, ej, idx])
        elif state == 3:
            attack[0] += 1
        return False
    
    # 빈 공간에 한 번씩 둬보기
    for idx, e in enumerate(empty):
        ei, ej = e
        past = arr[ei][ej]
        arr[ei][ej] = player

        # 가로 확인
        for j in range(3):
            count_state[arr[ei][j]] += 1
        # 상태 체크
        state = check_state(player, enemy, count_state)
        if do_state(state, ei, ej):
            return 'W'
        count_state = [0, 0, 0]

        # 세로 확인
        for i in range(3):
            count_state[arr[i][ej]] += 1
        # 상태 체크
        state = check_state(player, enemy, count_state)
        if do_state(state, ei, ej):
            return 'W'
        count_state = [0, 0, 0]

        # 대각선 확인 (왼쪽 위 => 오른쪽 아래)
        if ei == ej:
            for ij in range(3):
                count_state[arr[ij][ij]] += 1
            # 상태 체크
            state = check_state(player, enemy, count_state)
            if do_state(state, ei, ej):
                return 'W'
            count_state = [0, 0, 0]
        # 대각선 확인 (오른쪽 위 => 왼쪽 아래)
        if ei + ej == 2:
            for ij in range(3):
                count_state[arr[ij][2-ij]] += 1
            # 상태 체크
            state = check_state(player, enemy, count_state)
            if do_state(state, ei, ej):
                return 'W'
            count_state = [0, 0, 0]

            if attack[0] >= 2:
                attack.append([ei, ej])
                attack[0] = 0

        arr[ei][ej] = past

    # 방어할 게 2개 이상이면 진 것
    if len(shield) >= 2:
        return 'L'
    elif len(shield) == 1:
        si, sj, idx = shield[0]
        arr[si][sj] = player
        empty.pop(idx)
        return None
    else:
        if len(attack) > 1:
            return 'W'
        else:
            idx = len(empty) // 2
            ei, ej = empty[idx]
            arr[ei][ej] = player
            empty.pop(idx)
            return None


# 게임 플레이
if count[0] == 9:
    print('D')
else:
    is_turn = True
    while empty:
        if is_turn:
            result = play(player, enemy, empty)
            if result:
                print(result)
                break
        else:
            result = play(enemy, player, empty)
            if result:
                if result == 'W':
                    print('L')
                else:
                    print('W')
                break
        is_turn = not is_turn

    if not empty:
        print("D")
