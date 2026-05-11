def solution(genres, plays):
    genre_dict = {}
    song_dict = {}
    
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        
        # 장르별 총 재생 횟수 저장
        if genre in genre_dict:
            genre_dict[genre] += play
        else:
            genre_dict[genre] = play
        
        # 장르별 노래 목록 저장
        if genre in song_dict:
            song_dict[genre].append((play, i))
        else:
            song_dict[genre] = [(play, i)]
    
    sorted_genres = sorted(genre_dict.keys(), key=lambda x: genre_dict[x], reverse=True)
    
    answer = []
    
    for genre in sorted_genres:
        songs = song_dict[genre]
        
        songs.sort(key=lambda x: (-x[0], x[1]))
        
        for play, index in songs[:2]:
            answer.append(index)
    
    return answer
