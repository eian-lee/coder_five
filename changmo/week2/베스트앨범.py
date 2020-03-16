from collections import defaultdict

INDEX, GENRE, PLAY = 0, 0, 1
RECORD = 2
def solution(genres, plays):
    music_dic = defaultdict(list)
    count_dic = defaultdict(int)
    
    for index, music in enumerate(zip(genres, plays)):
        music_dic[music[GENRE]].append([index, music[PLAY]])
        count_dic[music[GENRE]] += music[PLAY]
    
    for genre in music_dic:
        music_dic[genre].sort(reverse=True, key=lambda x:x[PLAY])
        music_dic[genre] = [music[INDEX] for music in music_dic[genre]]
        
    result = []
    for music in sorted(count_dic.items(), key=lambda x: -x[PLAY]):
        result += music_dic[music[GENRE]][:RECORD]
    
    return result
