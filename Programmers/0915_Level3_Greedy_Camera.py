# 프로그래머스 Greedy Level 3 단속카메라
# 단속카메라 최소 개수 구하기
# Hanna 2020/09/15


# routes을 정렬하여 줄세우기


def solution(routes):
    answer = 1

    # 핵심 포인트
    routes.sort()

    right = routes[0][1]
    for a, b in routes:
        # 겹치는 부분 체크
        if a <= right:
            right = min(b, right)
        # 서로 겹쳐지지 않으면 새로이 체크
        else:
            right = b
            answer += 1

    return answer



print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))

