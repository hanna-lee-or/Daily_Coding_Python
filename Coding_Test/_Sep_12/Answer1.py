#카카오 코딩 테스트 1번
import string
import re

def solution(new_id):
    answer = ''

    #빈 문자열인 경우
    if (new_id == ''):
        return 'aaa'

    new_id = new_id.lower()
    array = re.findall(r"[a-z0-9_\.\-]+", new_id)

    new_id = ''
    for i in array:
        new_id += i

    flag = False
    temp_id = ''
    for i in range(len(new_id)):
        if(new_id[i] == '.'):
            if(flag == False):
                flag = True
                temp_id += new_id[i]
        else:
            flag = False
            temp_id += new_id[i]

    if(temp_id[0] == '.'):
        temp_id = temp_id[1:]
    if(len(temp_id) != 0):
        if(temp_id[-1] == '.'):
            temp_id = temp_id[:len(temp_id)-1]

    if(temp_id == ''):
        temp_id = 'aaa'
    elif(len(temp_id) >= 16):
        temp_id = temp_id[:15]
        if(temp_id[-1] == '.'):
            temp_id = temp_id[:len(temp_id)-1]
    elif(len(temp_id) <= 2):
        char = temp_id[-1]
        while len(temp_id) < 3:
            temp_id += char

    print(temp_id)
    answer = temp_id

    return answer


print(solution("...!@BaT#*..y.abcdefghijklm"))
