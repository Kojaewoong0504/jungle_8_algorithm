from collections import defaultdict


def solution(genres, plays):
    genre_count = defaultdict(int)
    album_dict = defaultdict(list)
    for i, (g,p) in enumerate(zip(genres, plays)):
        genre_count[g] += p
        album_dict[g].append((p, i))

    genre_order = sorted(genre_count.keys(), key=lambda g: -genre_count[g])

    answer = []
    for g in genre_order:
        top_two = sorted(album_dict[g], key=lambda x:(-x[0], x[1]))[:2]
        answer.extend(idx for _, idx in top_two)

    return answer