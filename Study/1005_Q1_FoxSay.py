# 백준 9536 / 여우는 어떻게 울지?

import sys

t = int(sys.stdin.readline().rstrip())
for i in range(t):
    sound = sys.stdin.readline().rstrip().split()

    info = sys.stdin.readline().rstrip()
    remove = []
    while info != 'what does the fox say?':
        animal = info.split()
        remove.append(animal[2])
        info = sys.stdin.readline().rstrip()

    result = ''
    for s in sound:
        if s not in remove:
            result += s + ' '
    print(result[:len(result) - 1])



