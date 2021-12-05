# 프로그래머스 Level1 로또의 최고 순위와 최저 순위
# 1부터 45까지의 숫자 중 6개를 찍어서 맞히는 대표적인 복권
# 알아볼 수 없는 번호를 0으로 표기하기로 하고,
# 당첨 가능한 최고 순위와 최저 순위

# 순서와 상관없이, 구매한 로또에 당첨 번호와 일치하는 번호가 있으면 맞힌 걸로 인정
# lottos는 길이 6인 정수 배열. 0 이상 45 이하인 정수.
# => 0은 알아볼 수 없는 숫자. 0 제외 중복 숫자 X. 정렬 X.


# 나의 답안.
def solution(lottos, win_nums):

    sd = set()
    # 당첨 번호 저장. hash 로 일치 여부 바로 확인할 수 있도록.
    for n in win_nums:
        sd.add(n)

    zero_cnt = 0
    win_cnt = 0
    for lt in lottos:
        if lt == 0:
            zero_cnt += 1
        elif lt in sd:
            win_cnt += 1
    print("z :", zero_cnt, "/ w :", win_cnt)

    # 최고 등수, 최저 등수
    best_rank = min(7 - win_cnt - zero_cnt, 6)
    worst_rank = min(7 - win_cnt, 6)

    return [best_rank, worst_rank]


# [3, 5]
# print("\n>> print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])) <<")
# print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
# [1, 6]
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
# [1, 1]
# print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))


# 다른 사람의 풀이
def solution_1(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans], rank[ans]


# 다른 사람의 풀이 (set 연산 활용)
# & : 교집합, | : 합집합, - : 차집합
def solution_2(lottos, win_nums):
    rank = {
        0: 6,
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1
    }
    return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)],
            rank[len(set(lottos) & set(win_nums))]]






