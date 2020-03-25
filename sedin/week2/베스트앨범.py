def solution(genres, plays):
    answer = []
    charts = {}

    for i, genre in enumerate(genres):
        if genre not in charts:
            charts.setdefault(genre, [])
            charts[genre].append(0)
        charts[genre].append([i, plays[i]])
        charts[genre][0] += plays[i]

    sorted_play_time = sorted(list(charts.values()), key=lambda k: k[0], reverse=True)

    while sorted_play_time:
        sorted_play_time[0].pop(0)
        sorted_play_time[0].sort(key=lambda k: k[1], reverse=True)
        for i in range(len(sorted_play_time[0])):
            if i >= 2:
                break
            answer.append(sorted_play_time[0][i][0])
        sorted_play_time.pop(0)

    return answer
