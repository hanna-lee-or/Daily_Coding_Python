# 프로그래머스 Challenge 쿠키 구입
# Hanna 2020/10/22
# 시간 초과 주의

# 과자가 든 바구니 N개
# 첫째 아들 i~m번 바구니/ 둘째 아들 m+1~r번
# 두 아들이 받을 과자 수 같아야 함
# 한 명의 아들에게 줄 수 있는 가장 많은 과자의 수 return
# 조건에 부합하지 않는 경우 0 return


# 나의 답. 시간 초과.
def solution(cookie):

    N = len(cookie)
    sum_list = [[0] * N for _ in range(N)]

    for i in range(N):
        sum_list[i][i] = cookie[i]

    # 구간 합 구하기
    for gap in range(1, N):
        for i in range(0, N-gap):
            sum_list[i][i+gap] = sum_list[i][i+gap-1] + sum_list[i+gap][i+gap]
    for a in range(N):
        print(sum_list[a])

    answer = 0
    # 쿠키 나누는 경우의 수 모두 돌려보기
    for start in range(N-2):
        for mid in range(N-2, start-1, -1):
            one = sum_list[start][mid]
            for end in range(N-1, mid, -1):
                print(start, mid, end)
                two = sum_list[mid+1][end]
                if one == two:
                    if answer < one:
                        answer = one
                    break
                elif one > two:
                    break

    return answer


print('\nanswer :', solution([1, 1, 2, 3]))