def solution(genres, plays):
    
    play_dic, total, best = {}, {}, []
    VALUE, COUNTS = 1, 0
    
    for i, play in enumerate(plays):
        play_dic[genres[i]] = play_dic.get(genres[i], []) + [(play,i)]
        total[genres[i]] = total.get(genres[i], 0) + play
    total = sorted(total.items(), key=lambda items:items[VALUE], reverse=True)
    
    for genre, _ in total:
        temp = sorted(play_dic[genre], key=lambda x:x[COUNTS], reverse=True)[:2]
        for _, song_idx in temp:
            best.append(song_idx)
    
    return best
