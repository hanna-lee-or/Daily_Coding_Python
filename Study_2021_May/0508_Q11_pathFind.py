# 프로그래머스 Level3 길 찾기 게임
# 이진트리를 구성하는 노드들의 좌표가 담긴 배열 nodeinfo가 매개변수로 주어질 때,
# 전위 순회, 후위 순회한 결과를 2차원 배열에 순서대로 담아 return

# 모든 노드는 서로 다른 x값을 가진다.
# 자식 노드의 y 값은 항상 부모 노드보다 작다.
# 임의의 노드 V의 left subtree 에 있는 모든 노드의 x값은 V의 x값 보다 작다.
# 임의의 노드 V의 right subtree 에 있는 모든 노드의 x값은 V의 x값 보다 크다.

# nodeinfo의 길이는 1 이상 10,000 이하
# nodeinfo[i] 는 i + 1번 노드의 좌표
# 모든 노드의 좌표 값은 0 이상 100,000 이하
# 트리의 깊이가 1,000 이하인 경우만 입력으로 주어진다.

import sys
sys.setrecursionlimit(10**6)


class Node:

    def __init__(self, dataList):
        # 루트 노드 찾기
        self.data = max(dataList, key=lambda x: x[1])
        # left subtree, right subtree 분류하기
        left_list = list(filter(lambda x: x[0] < self.data[0], dataList))
        right_list = list(filter(lambda x: x[0] > self.data[0], dataList))

        if left_list:
            self.left = Node(left_list)
        else:
            self.left = None

        if right_list:
            self.right = Node(right_list)
        else:
            self.right = None

    def preorder(self):

        traverse = []

        traverse.append(self.data[2])

        if self.left:
            traverse += self.left.preorder()

        if self.right:
            traverse += self.right.preorder()

        return traverse

    def postorder(self):

        traverse = []

        if self.left:
            traverse += self.left.postorder()

        if self.right:
            traverse += self.right.postorder()

        traverse.append(self.data[2])

        return traverse


class Tree:

    def __init__(self, root):
        self.root = root

    def preorder(self):

        if self.root:
            return self.root.preorder()

        else:
            return []

    def postorder(self):

        if self.root:
            return self.root.postorder()

        else:
            return []


# 나의 답.
def solution(nodeinfo):

    # print(list(zip(range(1, len(nodeinfo) + 1), nodeinfo)))
    nodeinfo = [x + [i+1] for i, x in enumerate(nodeinfo)]
    tree = Tree(Node(nodeinfo))

    return [tree.root.preorder(), tree.root.postorder()]


print(solution([[5, 3], [11, 5], [13, 3], [3, 5],
                [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))
# [ [7, 4, 6, 9, 1, 8, 5, 2, 3], [9, 6, 5, 8, 1, 4, 3, 2, 7] ]


# 다른 사람의 답. 트리를 그려나가며 순회 처리.
preorder = list()  # 귀찮아서 전역으로
postorder = list()


def solution_another(nodeinfo):
    levels = sorted(list({x[1] for x in nodeinfo}), reverse=True)  # 유효한 Y좌표
    # zip 함수를 이용해 노드 번호 붙이기 & 노드 정렬하기
    nodes = sorted(list(zip(range(1, len(nodeinfo)+1), nodeinfo)),
                   key=lambda x: (-x[1][1], x[1][0]))
    order(nodes, levels, 0)
    return [preorder, postorder]


def order(nodes, levels, curlevel):
    n = nodes[:]  # copy
    cur = n.pop(0)  # VISIT
    preorder.append(cur[0])  # PRE-ORDER
    if n:  # stop if leaf node
        for i in range(len(n)):  # find next floor
            if n[i][1][1] == levels[curlevel+1]:  # next floor
                if n[i][1][0] < cur[1][0]:  # LEFT CHILD
                    order([x for x in n if x[1][0] < cur[1][0]], levels, curlevel+1)
                else:  # RIGHT CHILD
                    order([x for x in n if x[1][0] > cur[1][0]], levels, curlevel+1)
                    break
    postorder.append(cur[0])  # POST-ORDER
