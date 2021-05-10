# 프로그래머스 Level2 프렌즈4블록
# 블록 4개가 붙어있을 경우 사라지면서 점수를 얻는 게임
# 같은 블록은 여러 2×2에 포함될 수 있으며, 한꺼번에 지워진다.
# 블록이 지워진 후에 위에 있는 블록이 아래로 떨어져 빈 공간을 채우게 된다.
# 지워지는 블록이 없을 때까지 반복한다.

# 입력으로 판의 높이 m, 폭 n과 판의 배치 정보 board 가 들어온다.
# 2 ≦ n, m ≦ 30
# 블록을 나타내는 문자는 대문자 A에서 Z가 사용된다.


def solution(m, n, board):

    l_board = ["" for _ in range(n)]
    # 중력이 (데이터 상에서는) 아래가 아니라 왼쪽으로 작용하도록 설정
    for s in board[::-1]:
        for i, c in enumerate(s):
            l_board[i] += c

    for s in l_board:
        print(s)

    # 4블록 체크 => 지우기(+블록 카운트) => 블록 이동시키기
    answer = 0
    end_flag = False
    # 게임 진행
    while not end_flag:
        count = 0
        remove_blocks = [set() for _ in range(n)]
        # 두 줄씩 비교
        for i in range(n-1):
            line_A = l_board[i]
            line_B = l_board[i+1]
            k = min(len(line_A), len(line_B))
            # 4블록 체크
            for j in range(k-1):
                if line_A[j] == line_A[j+1] and line_A[j:j+2] == line_B[j:j+2]:
                    remove_blocks[i].add(j)
                    remove_blocks[i].add(j+1)
                    remove_blocks[i+1].add(j)
                    remove_blocks[i+1].add(j+1)
        # 지우기(+블록 카운트) & 블록 이동시키기
        for i in range(n):
            for idx in remove_blocks[i]:
                count += 1
                l_board[i] = l_board[i][:idx] + "-" + l_board[i][idx+1:]
            l_board[i] = l_board[i].replace("-", "")
        # 지워진 블록이 없다면 게임 종료
        if count == 0:
            end_flag = True
        else:
            answer += count
        # 블록 상태
        print("---------------")
        for s in l_board:
            print(s)
        print(f"[{answer}]")

    return answer


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))  # 14
# print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))  # 15


# 다른 사람의 풀이.
def pop_num(b, m, n):
    pop_set = set()
    # search
    for i in range(1, n):
        for j in range(1, m):
            if b[i][j] == b[i - 1][j - 1] == b[i - 1][j] == b[i][j - 1] != '_':
                pop_set |= set([(i, j), (i - 1, j - 1), (i - 1, j), (i, j - 1)])
    # set_board
    for i, j in pop_set:
        b[i][j] = 0
    for i, row in enumerate(b):
        empty = ['_'] * row.count(0)
        b[i] = empty + [block for block in row if block != 0]
    return len(pop_set)


def solution_another(m, n, board):
    count = 0
    b = list(map(list, zip(*board)))  # 행열 바꿔치기
    while True:
        pop = pop_num(b, m, n)
        if pop == 0:
            return count
        count += pop
