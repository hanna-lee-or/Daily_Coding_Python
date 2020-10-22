# 백준 1991 / 트리 순회
# 트리 전위 순회, 중위 순회, 후위 순회한 결과 출력하기
# 루트 노드는 항상 A
# 각 줄에 N개의 알파벳을 공백 없이 출력

# 답지 참고, 재귀 함수 이용해
# 트리 순회 진행한다는 점 기억하기!

import sys


# 전위 순회
def preorder(node):
    print(node.item, end='')
    if node.lchild != '.':
        preorder(tree[node.lchild])
    if node.rchild != '.':
        preorder(tree[node.rchild])


# 중위 순회
def inorder(node):
    if node.lchild != '.':
        inorder(tree[node.lchild])
    print(node.item, end='')
    if node.rchild != '.':
        inorder(tree[node.rchild])


# 후위 순회
def postorder(node):
    if node.lchild != '.':
        postorder(tree[node.lchild])
    if node.rchild != '.':
        postorder(tree[node.rchild])
    print(node.item, end='')


class Node:
    def __init__(self, item, lchild, rchild):
        self.item = item
        self.lchild = lchild
        self.rchild = rchild


n = int(sys.stdin.readline().rstrip())
tree = dict()
# 트리 그리기
for i in range(n):
    A, B, C = sys.stdin.readline().rstrip().split()
    tree[A] = Node(item=A, lchild=B, rchild=C)

# 순회
preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])
print()

