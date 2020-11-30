# leetcode 310 Minimum Height Trees
# 가장 낮은 높이로 트리를 구성할 때 Root가 될 수 있는 노드 구하기

# 아이디어 안 떠올라서 답지 분석 진행!

from collections import defaultdict
from collections import deque


# 구글에 있는 답안 (Runtime 224ms)
class Solution:
    def findMinHeightTrees(self, n: int, edges: list) -> list:
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # 노드가 하나일 때
        if n == 1:
            return [0]

        leaves = defaultdict(set)
        # 그래프 그리기
        for u, v in edges:
            leaves[u].add(v)
            leaves[v].add(u)
        que = deque()
        # 연결선이 하나인 노드 큐에 삽입
        print(f'1차 큐 ')
        for u, vs in leaves.items():
            if len(vs) == 1:
                que.append(u)
                print(u, end=' ')
        print()
        # 큐에 따른 처리 진행
        while n > 2:
            _len = len(que)
            n -= _len
            for _ in range(_len):
                u = que.popleft()
                # 큐에서 하나 꺼냄.
                # 해당 노드의 연결 노드 확인
                for v in leaves[u]:
                    # 큐에는 잎사귀부터 들어가게 됨.
                    # 잎사귀들 지워나감.
                    leaves[v].remove(u)
                    # 겉 잎사귀들이 제거되면 다음 잎사귀로 들어감.
                    if len(leaves[v]) == 1:
                        que.append(v)
        return list(que)


print(Solution().findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]))

