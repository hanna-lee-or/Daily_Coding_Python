# 프로그래머스 Level3 다단계 칫솔
# 판매원에게 배분된 이익금의 총합을 계산하여(정수형으로),
# 입력으로 주어진 enroll에 이름이 포함된 순서에 따라 나열하면 됩니다.

# 민호는 센터이며, enroll에 민호의 이름은 없습니다.
# enroll 에 등장하는 이름은 조직에 참여한 순서에 따릅니다.

# seller 에는 같은 이름이 중복해서 들어있을 수 있습니다.
# 칫솔 한 개를 판매하여 얻어지는 이익은 100 원입니다.
# 모든 조직 구성원들의 이름은 10 글자 이내의 영문 알파벳 소문자들로만 이루어져 있습니다.

# 이름이 같다고 해서 판매수량을 합산하여 계산하면 안되고 별개로 보고 계산해야한다.


from collections import defaultdict


# 나의 답안.
def solution(enroll, referral, seller, amount):
    answer = []

    profit_dict = defaultdict(list)
    total_dict = defaultdict(int)

    # 개별 연필 수익금 체크
    for i, name in enumerate(seller):
        profit_dict[name].append(amount[i] * 100)
    print(profit_dict)

    # 하위 조직원부터 자신의 수익금의 10%를 위로 상납.
    n = len(enroll) - 1
    for i in range(n, -1, -1):
        target = enroll[i]
        superior = referral[i]

        # 상납금을 위로 보내고 큐에 쌓아둠.
        while profit_dict[target]:
            profit = profit_dict[target].pop()
            r = profit // 10
            if r != 0:
                profit_dict[superior].append(r)
            total_dict[target] += profit - r


    # 답안 작성
    for e in enroll:
        answer.append(total_dict[e])

    return answer


# 답 : [360, 958, 108, 0, 450, 18, 180, 1080]
print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["young", "young", "john", "tod", "emily", "mary"],
               [5, 12, 4, 2, 5, 10]))
# 답 : [0, 110, 378, 180, 270, 450, 0, 0]
"""
print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["sam", "emily", "jaimie", "edward"],
               [2, 3, 5, 4]))
"""


# 다른 사람의 풀이.
def solution_another(enroll, referral, seller, amount):
    graph, ans = {}, {e: 0 for e in enroll}

    for e, r in zip(enroll, referral):
        graph[e] = r
    print(graph)


    for s, a in zip(seller, amount):
        money = a * 100
        rate = money // 10
        ans[s] += money - rate
        x = graph[s]

        # 타고 올라가는 형식
        while x != "-":
            if rate == 0:
                break
            ans[x] += rate - rate // 10
            rate //= 10
            x = graph[x]

    return list(ans.values())


# 답 : [360, 958, 108, 0, 450, 18, 180, 1080]
"""
print(solution_another(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
                       ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
                       ["young", "john", "tod", "emily", "mary"],
                       [12, 4, 2, 5, 10]))
"""
