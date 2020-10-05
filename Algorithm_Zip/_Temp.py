#사각형 좌표 찾기


import collections


def solution(v):
    answer = []

    for i in zip(*v):
        y = collections.Counter(i)
        answer.extend([i for i in y if y[i] == 1])

    return answer