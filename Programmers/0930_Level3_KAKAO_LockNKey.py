# 프로그래머스 2020 KAKAO Level 3 자물쇠와 열쇠
# 자물쇠를 열쇠로 열 수 있는가. 열쇠는 회전, 이동 가능.
# Hanna 2020/09/30

# 키는 항상 자물쇠보다 작거나 같다.
# key_up 회전 후 정렬 안해서 뻘짓...

# 행렬을 확장시켜서 key 행렬과 lock 행렬을 체크하는 방법도 있음!


# 나의 답
def solution(key, lock):

    n = len(lock)
    m = len(key)

    # key의 돌기 부분, lock의 홈 부분 체크
    key_up = []
    lock_down = []
    for i in range(n):
        for j in range(n):
            if lock[i][j] == 0:
                lock_down.append([i, j])
    for i in range(m):
        for j in range(m):
            if key[i][j] == 1:
                key_up.append([i, j])
    # key의 돌기 부분이 lock의 홈보다 적을 때 = False
    if len(key_up) < len(lock_down):
        return False
    elif len(lock_down) == 0:
        return True

    print("key :", key_up)
    print("lock :", lock_down)

    # 90도 회전
    def rotate_90(matrix):
        ret = []
        for mi, mj in matrix:
            ret.append([mj, m - 1 - mi])
        # ㅎㅎ...ㅎㅎㅎㅎ
        ret.sort()
        return ret

    # 키의 돌기부분과 자물쇠의 홈부분만 체크
    # 키 이동 시, 돌기부분만 이동해서 체크!
    def check_pattern(n, m, key_up, lock_down):
        hole = len(lock_down)
        limit = n
        # [-(m-1), +(n+m-1)] ~ [+(m-1), -(n+m-1)] <= 이동 범위
        # i는 세로 이동, j는 가로 이동
        for i in range(-m+1, n):
            for j in range(-m+1, n):
                # key 이동
                key_mask = []
                for ki, kj in key_up:
                    move = [ki + i, kj + j]
                    if 0 <= move[0] < limit and 0 <= move[1] < limit:
                        key_mask.append(move)
                #  key와 lock 체크
                if len(key_mask) != hole:
                    continue
                flag = True
                # 이 부분 때문에 key_up은 정렬되어 있어야 함! ☆
                for k in range(hole):
                    if key_mask[k] != lock_down[k]:
                        flag = False
                        break
                if flag:
                    print(i, j, key_mask)
                    return True
        return False

    answer = False
    for r in range(4):
        print(r, "key :", key_up)
        if check_pattern(n, m, key_up, lock_down):
            answer = True
            break
        else:
            key_up = rotate_90(key_up)

    return answer


print('\nanswer :', solution([[0, 0, 0], [1, 0, 1], [0, 1, 1]],
                             [[1, 1, 0], [1, 1, 1], [1, 1, 0]]))
