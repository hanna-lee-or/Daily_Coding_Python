# 프로그래머스 Level2 조이스틱 (탐욕법)
# 조이스틱으로 알파벳 이름을 완성하세요.
# [!] 맨 처음엔 A로만 이루어져 있습니다.
# name은 알파벳 대문자로만 이루어져 있습니다.
# name의 길이는 1 이상 20 이하입니다.

# 문제 의도는 탐욕법 (그리디 알고리즘) 사용하는건데
# 그리디 사용하면 정답처리는 되나
# 항상 최적의 해가 나오는 것은 아님. 뭔가 문제가...음...


def solution(name):
    visited = [0] * len(name)

    for i, c in enumerate(name):
        visited[i] = setLetter(c)

    print(visited)

    idx = 0
    answer = 0

    # 조이스틱 움직이기, 오른쪽 이동 or 왼쪽 이동
    while True:
        answer += visited[idx]
        visited[idx] = 0
        if sum(visited) == 0:
            return answer

        print(idx, end=' => ')

        # 이동 방향 정하기
        left, right = 1, 1
        while visited[idx - left] == 0:
            left += 1
        while visited[idx + right] == 0:
            right += 1
        # 위치 조정
        if left < right:
            answer += left
            idx -= left
        else:
            answer += right
            idx += right


# 알파벳 조정 & 조이스틱 움직이는 횟수 반환
def setLetter(target) -> int:
    if target == 'A':
        return 0
    up = ord(target) - ord('A')
    down = ord('Z') - ord(target) + 1
    return min(up, down)


print(solution("JEROEN"))  # 56
# print(solution("JAN"))  # 23
# print(solution("BAAAAAB"))  # 3
