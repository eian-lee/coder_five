def solution(genres, plays):
    sorted_genres = {}
    for genre in set(genres):
        sorted_genres[genre] = sum([play for g, play in zip(genres, plays) if genre == g])
    sorted_genres = sorted(sorted_genres.items(), key=lambda x: x[1], reverse=True)

    new_dict = {}
    plays = list(enumerate(plays))
    answer = []
    for genre, _ in sorted_genres:
        new_dict[genre] = [play for g, play in zip(genres, plays) if genre == g]
        new_dict[genre] = sorted(new_dict[genre], key=lambda x: x[1], reverse=True)
        answer.extend(idx for idx, _ in new_dict[genre][:2])
    return answer