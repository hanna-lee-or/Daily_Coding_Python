# 프로그래머스 그래프 Level 3 순위
# 정확하게 순위를 매길 수 있는 선수의 수
# Hanna 2020/09/28

# ☆부분이 핵심! 아이디어는 다른 사람 참고.
# 처음에는 부모 노드들을 세고 자식 노드들을 세려 함. (부모의 부모, 자식의 자식 포함해서)
# 하지만 어떻게 세야하지 하다가 다른 분이 set()을 활용한 걸 참고했다.


def solution(n, results):
    answer = 0

    # graph_win, graph_lose = defaultdict(set), defaultdict(set)
    # defaultdict()을 사용하여 사전의 객체 타입을 정할 수 있음.
    graph_win = {}
    graph_lose = {}

    for i in range(1, n+1):
        graph_win[i] = set()
        graph_lose[i] = set()

    # 그래프 만들기 (dictionary 이용)
    for a, b in results:
        graph_win[a].add(b)
        graph_lose[b].add(a)

    print("w :", graph_win)
    print("l :", graph_lose)

    # ☆
    for i in range(1, n+1):
        # i 선수에게 이긴 선수 w는
        # i 선수에게 진 사람들을 w의 진 사람 목록에 추가한다.
        for w in graph_win[i]:
            graph_lose[w].update(graph_lose[i])
        # i 선수에게 진 선수 l은
        # i 선수에게 이긴 사람들을 l의 이긴 사람 목록에 추가한다.
        for l in graph_lose[i]:
            graph_win[l].update(graph_win[i])

    print("w :", graph_win)
    print("l :", graph_lose)

    # 이긴 사람 수 + 진 사람 수 == n - 1 이면 순위 판별 O
    for i in range(1, n+1):
        win = len(graph_win[i])
        lose = len(graph_lose[i])
        if win + lose == n - 1:
            answer += 1

    return answer


print('\nanswer :', solution(5, [[4, 3], [4, 2],
                                 [3, 2], [1, 2], [2, 5]]))
