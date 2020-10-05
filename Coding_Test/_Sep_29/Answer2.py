# 11번가 코딩테스트 2
# Hanna 2020/09/29

# 메모


def solution(S):
    answer = []

    n = len(S)
    m = len(S[0])

    # 두 개씩 비교
    for i in range(n):
        for j in range(i+1, n):
            a = S[i]
            b = S[j]
            # 길이별 비교
            for c in range(m):
                if a[c] == b[c]:
                    answer.append(i)
                    answer.append(j)
                    answer.append(c)
                    return answer

    return answer


print('\nanswer :', solution(['zzzz', 'ferz', 'zdsr', 'fgtd'] ))

