# 11번가 코딩테스트 3
# Hanna 2020/09/29

# 리스트에 1~N 까지 한번씩 나오게 하시오.


def solution(A):

    n = len(A) + 1
    A.sort()
    # All must be 1.
    check_list = [0] * n

    for i in A:
        check_list[i] += 1
    print('A :', A)
    print('>', check_list)

    flag = 0
    count = 0
    # i가 j한테 숫자 나눠주는 거
    for i in range(1, n):
        if check_list[i] == 1:
            continue
        flag = check_list[i] - 1
        # look left
        for j in range(1, i):
            target = check_list[i-j]
            if target == 1:
                continue
            elif target == 0:
                if flag > 0:
                    flag -= 1
                    check_list[i] -= 1
                    check_list[i-j] += 1
                    count += j
            else:
                if flag < 0:
                    while check_list[i-j] == 1 or flag == 0:
                        flag += 1
                        check_list[i] += 1
                        check_list[i-j] -= 1
                        count += j
            if count > 1e9:
                return -1
        print('i', i, 'f', flag)
        # look right
        for j in range(i+1, n):
            target = check_list[j]
            if target == 1:
                continue
            elif target == 0:
                if flag > 0:
                    flag -= 1
                    check_list[i] -= 1
                    check_list[j] += 1
                    count += j - i
            else:
                if flag < 0:
                    while check_list[j] == 1 or flag == 0:
                        flag += 1
                        check_list[i] += 1
                        check_list[j] -= 1
                        count += j - i
            if count > 1e9:
                return -1

    print('>', check_list)

    return count


print('\nanswer :', solution([1, 1, 3, 5, 5]))
