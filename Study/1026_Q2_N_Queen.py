# SW Expert Academy 2806 / N-Queen
# 백트래킹 같은데...
# 답지 참고 @ㅁ@... 분석 중...

# N*N 보드에 N개의 퀸을
# 서로 다른 두 퀸이 공격하지 못하게 놓는 경우의 수


import sys


# 대각선 체크 함수 (idx 현재, c 다음)
# True면 대각선이 겹치는 상태
# 대각선이 겹치면 인덱스 x, y의 합이 같다는 규칙 존재
def possible(idx, c):
    for i in range(idx):
        # 행과 열의 차이가 같다면.
        # x축 차이와 y축의 차이가 같은지 보면 됨.
        # map_list[i] : i행에 위치한 퀸의 위치 열(x)
        # idx - i : y축 차이
        if idx - i == abs(c - map_list[i]):
            return True
    return False


# 퀸 놓아보기
def dfs(idx):

    # 마지막 행에 다다르면
    # 경우의 수 카운트
    if idx == N:
        global answer
        answer += 1
        print(map_list)
        return

    # 행마다 위치 탐색 실행
    # N개의 퀸이 N*N 크기 체스판에 있으므로
    # 퀸들이 각 행마다 반드시 1개씩 존재해야 함.
    # 즉, 열과 대각선만 추가로 체크해주면 됨.
    for i in range(N):
        # 이미 사용한 열이라면 넘어감
        if visit[i]:
            continue
        # 대각선이 겹친다면 넘어감
        if possible(idx, i):
            continue
        # 위치시킨 자리 표시
        visit[i] = 1
        map_list[idx] = i
        # 다음 퀸 자리 탐색
        dfs(idx + 1)
        # dfs 함수 끝까지 갔다가 되돌아오면
        # 되돌아올 때 회수한 퀸 위치 표시
        visit[i] = 0


# 첫 번째 퀸을 모든 칸에 한 번씩 놓아보며
# 경우의 수 찾아가기
for t in range(1, int(input()) + 1):
    N = int(input())
    map_list = [0 for _ in range(N)]
    visit = [0 for _ in range(N)]
    answer = 0
    dfs(0)
    print('#{} {}'.format(t, answer))
