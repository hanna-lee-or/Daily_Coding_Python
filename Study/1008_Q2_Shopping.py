# 프로그래머스 KAKAO 보석 쇼핑
# 모든 종류의 보석을 포함하는 가장 짧은 구간 찾기
# 시간 효율성 고려 필요

# 답안 참고. 투 포인터 사용 O(n).

from collections import defaultdict


def solution(gems):

    answer = [0, 0]
    candidates = []
    start, end = 0, 0
    gems_len, gem_kind = len(gems), len(set(gems))
    gems_dict = defaultdict(lambda: 0)

    while True:
        kind = len(gems_dict)
        # start 지점이 끝에 다다르면 종료
        if start == gems_len:
            break
        # 모든 종류의 보석이 존재하면 후보군으로 선정
        if kind == gem_kind:
            candidates.append((start, end))
            # 시작 지점 + 1, 시작 지점 보석 종류 개수 - 1
            # 해당 보석의 개수가 0이면 gems_dict에서 제거
            gems_dict[gems[start]] -= 1
            if gems_dict[gems[start]] == 0:
                del gems_dict[gems[start]]
            start += 1
            continue
        # end 지점이 끝에 다다르면 종료
        if end == gems_len:
            break
        # 모든 종류의 보석이 존재하지 않으면 end + 1
        if kind != gem_kind:
            # 끝 지점 + 1, 끝 지점 보석 종류 개수 + 1
            gems_dict[gems[end]] += 1
            end += 1
            continue

    length = float('inf')   # 무한히 큰 값을 가진 변수로 설정
    # 후보군 중 가장 짧은 구간 선택
    for s, e in candidates:
        if length > e - s:
            length = e - s
            answer[0] = s + 1
            answer[1] = e

    return answer


print(solution(["AA", "AB", "AC", "AA", "AC"]))


