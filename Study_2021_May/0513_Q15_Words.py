# 프로그래머스 Level2 영어 끝말잇기
# n명의 사람이 영어 끝말잇기를 하고 있다.
#  1. 1번부터 번호 순서대로 돌아가며 한 사람씩 차례대로 단어를 말합니다.
#  2. 앞사람이 말한 단어의 마지막 문자로 시작하는 단어를 말해야 합니다.
#  3. 이전에 등장했던 단어, 한 글자 단어는 사용할 수 없습니다.
# 사람의 수 n과 사람들이 순서대로 말한 단어 words 가 매개변수로 주어질 때,
# 가장 먼저 탈락하는 사람의 번호와 그 사람이 자신의 몇 번째 차례에 탈락하는지를 구하라.

# n은 2 이상 10 이하
# words 배열의 길이는 n 이상 100 이하
# 단어의 길이는 2 이상 50 이하
# 모든 단어는 알파벳 소문자로만 이루어져 있다.
# 정답은 [ 번호, 차례 ] 형태로 return
# 탈락자가 생기지 않는다면, [0, 0]을 return

import pprint


def solution(n, words):

    words_set = set()

    pre = words[0][0]
    for i, w in enumerate(words):
        if w in words_set or w[0] != pre:
            turn, target = divmod(i, n)
            return [target+1, turn+1]
        pre = w[-1]
        words_set.add(w)

    return [0, 0]


print(solution(3, ["tank", "kick", "know", "wheel", "land",
                   "dream", "mother", "robot", "tank"]	))  # [3, 3]
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize",
                   "encourage", "ensure", "establish", "hang", "gather",
                   "refer", "reference", "estimate", "executive"]))  # [0, 0]
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))  # [1, 3]


# 다른 사람의 풀이
def solution_another(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]
