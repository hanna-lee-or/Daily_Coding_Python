# 백준 9935 / 문자열 폭발
# 시간 초과에 주의
# join 문법 알아두기!

import sys

# 문자열 s, 폭발 문자열 bomb
s = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()
sn = len(s)
bn = len(bomb)


# 나의 답 ('끝문자'와 같을 때 확인. 커서 옮겨서 덮어씌우기가 포인트!)
def solution(s, bomb, sn, bn):

    idx = 0
    cursor = 0
    target_c = bomb[-1]
    answer = ['' for _ in range(sn)]
    while idx < sn:
        answer[cursor] = s[idx]
        if answer[cursor] == target_c and cursor >= bn-1:
            if "".join(answer[cursor-bn+1:cursor+1]) == bomb:
                cursor -= bn
        idx += 1
        cursor += 1

    if cursor == 0:
        return "FRULA"
    else:
        return "".join(answer[:cursor])


print(solution(s, bomb, sn, bn))
