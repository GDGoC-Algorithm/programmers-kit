def solution(genres, plays):
    # 1. 장르별 총 재생 횟수와 장르별 곡 정보를 담을 딕셔너리 준비
    genre_total = {}
    genre_songs = {}
    
    for i in range(len(genres)):
        g = genres[i]
        p = plays[i]
        
        # 장르별 총합 누적
        genre_total[g] = genre_total.get(g, 0) + p
        
        # 장르별 곡 정보 추가
        if g not in genre_songs:
            genre_songs[g] = []
        genre_songs[g].append((i, p))
        
    # 2. 총 재생 횟수가 많은 장르 순으로 정렬
    sorted_genres = sorted(genre_total.items(), key=lambda x: x[1], reverse=True)
    
    answer = []
    
    # 3. 정렬된 장르 순서대로 곡을 2개씩 추출
    for g, total in sorted_genres:
        # 해당 장르의 곡들을 재생 횟수 내림차순, 인덱스 오름차순으로 정렬
        songs = sorted(genre_songs[g], key=lambda x: (-x[1], x[0]))
        
        # 최대 2개까지 정답 리스트에 추가
        answer.extend([s[0] for s in songs[:2]])
        
    return answer
