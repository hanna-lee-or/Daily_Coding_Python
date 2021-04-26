# 프로그래머스 Level2 전화번호 목록
# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false 를 반환

class Node:
    def __init__(self, data):
        self.data = data
        self.child = []
        self.end_flag = False

    def __str__(self):
        return str(self.data)

    def __cmp__(self, other):
        if self.data < other.data:
            return -1
        elif self.data == other.data:
            return 0
        else:
            return 1

    def getChildIdx(self, data) -> int:
        child_len = len(self.child)
        if child_len > 0:
            for i, c in enumerate(self.child):
                if c.data == data:
                    return i
        return -1


class Tree:
    def __init__(self):
        self.root = None


# 다진 트리(m-ary Tree)를 이용한 풀이.
# 각 전화번호의 끝나는 부분은 end_flag 로 표시한다.
# 이 때 접두사가 되는 번호가 있으면 end_flag 를 만나게 된다.
# 접두사가 되는 번호라면 끝나는 노드 이후로도 자식 노드가 존재한다.
def solution(phone_book):

    phone_tree = Tree()
    phone_tree.root = Node("$")

    for phone in phone_book:
        node = phone_tree.root
        for c in phone:
            idx = node.getChildIdx(c)
            if len(node.child) <= 0 or idx < 0:
                node.child.append(Node(c))
                node = node.child[-1]
            else:
                node = node.child[idx]
            print(node, end=' ')
            # 도중에 end_flag 를 만나면 false
            if node.end_flag:
                return False
        # 끝난 지점 이후 노드 존재 시 false
        if len(node.child) > 0:
            return False
        node.end_flag = True
        print(f"/ [{node}]")

    return True


# print(solution(["119", "97674223", "1195524421"]))
# print("---")
print(solution(["123", "456", "789"]))


# 다른 사람의 풀이. 해쉬 사용. (정석 풀이)
def solution_another_hash(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
# << 댓글 발췌 >>
# 전화번호 길이에 제한이 없으면 O(N^2)인데, 20자 제한이 있으니까 O(N)입니다. //
# sort 사용한 방식이나 이 방식이나 시간복잡도는 같은데 확실히 해쉬가 접근이 빠르네요.


# 다른 사람의 풀이. 정렬 사용.
def solution_another_sorted(phone_book):
    phone_book = sorted(phone_book)

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True
# << 댓글 발췌 >>
# string을 그냥 정렬하면 앞의 글자 순서대로 정렬이 되나봐요. //
# 시간복잡도로는 sort 한 번하고 다음 문자열과 비교하는 것이 O(nlogn)으로
# 이중반복문 돌리는 O(n^2)보다 좋은게 맞습니다.
# 다만 제출했을 때 이중반복문의 수행시간이 더 낮게 나오는 것은
# 테스트 케이스에 사용된 데이터가 원인으로 보입니다.
