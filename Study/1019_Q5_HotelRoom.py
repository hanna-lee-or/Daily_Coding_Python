# 프로그래머스 KAKAO 호텔방 배정
# Hanna 2020/10/21
# 시간 초과 주의

# 한 번에 한 명씩 신청한 순서대로 방 배정
# 고객은 투숙하기 원하는 방 번호 제출
# 고객이 원하는 방이 비어 있다면 즉시 배정
# 이미 배정된 방이면, 번호가 큰 방 중 가장 번호가 작은 방 배정

# 전체 방 개수 k, 고객 위시 리스트 room_number
# 고객에게 배정되는 방 번호 순서대로 담아 return


import sys
sys.setrecursionlimit(10**6)


# 다른 사람의 답. visit 변수를 이용하여
# 거쳐간 모든 방의 다음 방을 업데이트 함.
def solution_another(k, room_number):
    room_dic = {}
    ret = []
    for i in room_number:
        n = i
        visit = [n]
        while n in room_dic:
            n = room_dic[n]
            visit.append(n)
        ret.append(n)
        for j in visit:
            room_dic[j] = n+1
    return ret


# 나의 답. 시간 초과.
def solution(k, room_number):

    check_recent = dict()
    answer = []

    for r in room_number:
        if r not in check_recent:
            check_recent[r] = r+1
            answer.append(r)
            print(r, r, "--")
        else:
            cursor = check_recent[r]
            while cursor in check_recent:
                print(r, cursor)
                cursor = check_recent[cursor]
            answer.append(cursor)
            print(r, cursor, "--")
            check_recent[cursor] = cursor+1
            check_recent[r] = cursor+1

    return answer


print('\nanswer :', solution(10, [1, 3, 4, 1, 3, 1]))
