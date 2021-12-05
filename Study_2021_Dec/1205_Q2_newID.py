# 프로그래머스 Level1 신규 아이디 추천
# 카카오 서비스에 가입하는 유저들의 아이디를 생성하는 업무 담당
# 아이디 규칙에 맞지 않는 아이디를 입력했을 때,
# 유사하면서 규칙에 맞는 아이디를 추천해주는 프로그램을 개발

# 아이디의 길이는 3자 이상 15자 이하
# 아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용
# 마침표(.)는 처음, 끝, 연속으로 사용할 수 없음

# "네오"는 다음과 같이 7단계의 순차적인 처리 과정을 통해 검사 및 추천
# [1단계] 소문자로 치환
# [2단계] 비허용 문자 제거
# [3단계] 연속 마침표(.) 를 하나의 마침표(.)로 치환
# [4단계] 처음, 끝의 마침표(.) 제거
# [5단계] 빈 문자열이면 "a" 대입
# [6단계] 길이가 16자 이상이면, 첫 15개 문자 제외 제거 => 끝이 마침표(.) 이면 제거
# [7단계] 길이가 2자 이하이면, 마지막 문자를 길이가 3이 될 때까지 반복

import re

# 나의 답안.
def solution(new_id):

    # [1단계]
    new_id = new_id.lower()
    # [2단계] => re.sub('[^a-z0-9\-_.]', '', st)
    new_id = "".join(re.findall('[a-z0-9-_.]+', new_id))
    # [3단계] => re.sub('\.+', '.', st)
    new_id = re.sub('[.]+', '.', new_id)
    # [4단계] => re.sub('^[.]|[.]$', '', st)
    new_id = new_id[1:] if len(new_id) > 0 and new_id[0] == '.' else new_id
    new_id = new_id[:-1] if len(new_id) > 0 and new_id[-1] == '.' else new_id
    # [5단계] => st = 'a' if len(st) == 0 else st[:15]
    if new_id == '':
        new_id = 'a'
    # [6단계] => st = re.sub('^[.]|[.]$', '', st)
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    # [7단계]
    elif len(new_id) <= 2:
        c = new_id[-1]
        while len(new_id) < 3:
            new_id += c

    return new_id


# "bat.y.abcdefghi"
# print("\n>> print(solution(\"...!@BaT#*..y.abcdefghijklm\")) <<")
# print(solution("...!@BaT#*..y.abcdefghijklm"))

# "z--"
# print(solution("z-+.^."))
# "aaa"
# print(solution("=.="))
# "123_.def"
# print(solution("123_.def"))
# "abcdefghijklmn"
# print(solution("abcdefghijklmn.p"))
# "bbb"
print(solution("................b"))


# 다른 사람의 풀이
def solution_1(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st

