# 프로그래머스 2019 KAKAO Level 2 오픈채팅방
# 오픈채팅방 상태 기록
# Hanna 2020/09/27


# 다른 사람의 답 (이름표 작성 후, 기록 작성)
def solution_another(record):
    answer = []
    namespace = {}
    printer = {'Enter': '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}
    for r in record:
        rr = r.split(' ')
        if rr[0] in ['Enter', 'Change']:
            namespace[rr[1]] = rr[2]

    for r in record:
        if r.split(' ')[0] != 'Change':
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

    return answer


# 나의 답 (이름표 및 출입 상태 기록, 기록 string화)
def solution(record):
    answer = []

    name = dict()
    monitorID = []
    monitorState = []
    for i, r in enumerate(record):
        state = r.split()
        if state[0] == "Enter":
            # 들어온 경우
            name[state[1]] = state[2]
            monitorID.append(state[1])
            monitorState.append(0)
        elif state[0] == "Leave":
            # 나간 경우
            monitorID.append(state[1])
            monitorState.append(1)
        else:
            # 이름 수정
            name[state[1]] = state[2]

    for i in range(len(monitorID)):
        str = name[monitorID[i]]
        if monitorState[i] == 0:
            str += "님이 들어왔습니다."
        else:
            str += "님이 나갔습니다."
        answer.append(str)

    return answer


print('\nanswer :', solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo",
                              "Leave uid1234", "Enter uid1234 Prodo",
                              "Change uid4567 Ryan"]))
