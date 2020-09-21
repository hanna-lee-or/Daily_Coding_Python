# 프로그래머스 해시 Level 3 베스트 앨범
# 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범 출시
# Hanna 2020/09/21

# 으악 장르별 두 곡씩을, TOP2 장르 두 곡씩으로 알아들어서 계속 틀림ㅠㅠ


# 다른 사람의 답
def another(genres, plays):
    answer = []
    dic = {e: [] for e in set(genres)}
    # zip() => 동일한 개수로 이루어진 자료형을 묶어줌.
    for genre, play, l in zip(genres, plays, range(len(plays))):
        dic[genre].append([play, l])
    # lambda 속 lambda => 바로 정렬!
    genre_sort = sorted(dic.keys(),
                        # key=lambda x: sum([t[0] for t in d[x]])
                        key=lambda x: sum(map(lambda y: y[0], dic[x])),
                        reverse=True)
    for g in genre_sort:
        temp = [e[1] for e in sorted(dic[g], key=lambda x: (x[0], -x[1]), reverse=True)]
        answer += temp[:min(len(temp), 2)]
    return answer


# 나의 답
def solution(genres, plays):
    answer = []
    album = {}

    # 앨범 정보 기록 (dictionary 이용)
    for i in range(len(genres)):
        album[genres[i]] = album.get(genres[i], []) + [(plays[i], i)]

    # 많이 재생된 순으로 정렬 (재생 수가 같으면 고유번호가 낮은 순으로)
    for j in album.keys():
        album[j].sort(key=lambda x: (x[0], -x[1]), reverse=True)
    print(album)

    # 장르 재생 횟수 카운트
    count_list = []
    for genre in album:
        count = 0
        for play in album[genre]:
            count += play[0]
        count_list.append((count, genre))
    count_list = sorted(count_list, reverse=True)
    print(count_list)

    # 장르별 두 곡씩
    for c in count_list:
        best_genre = album[c[1]]
        answer.append(best_genre[0][1])
        if len(best_genre) > 1:
            answer.append(best_genre[1][1])

    return answer


print('\nanswer :', solution(["pop", "classic", "pop", "classic", "classic", "pop"],
                             [600, 500, 600, 150, 800, 2500]))

print('\nanswer+ :', another(["pop", "classic", "pop", "classic", "classic", "pop"],
                             [600, 500, 600, 150, 800, 2500]))
