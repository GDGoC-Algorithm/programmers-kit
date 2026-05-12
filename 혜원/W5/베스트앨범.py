# 적용 알고리즘의 개념
    # 해시(딕셔너리) + 정렬
    # 장르별 총 재생 수를 모으고,
    # 각 장르 안에서 노래를 정렬해서 상위 2개만 고름

# 문제 풀이를 위한 접근 방식(or 개념) 설명
    # 1. 장르별 총 재생 수를 구하고
    # 2. 장르별 노래 목록을 저장한 뒤
    # 3. 장르는 총 재생 수 내림차순으로 정렬
    # 4. 각 장르 안에서는 재생 수 내림차순, 같으면 고유번호 오름차순으로 정렬
    # 5. 앞에서 2개만 뽑음


def solution(genres, plays):
    genre_total = {} # 장르별 총 재생 수
    genre_songs = {} # 장르별 노래 목록 -> (재생 수, 고유번호)

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]

        if genre not in genre_total:
            genre_total[genre] = 0
            genre_songs[genre] = []

        genre_total[genre] += play
        genre_songs[genre].append((play, i))

    sorted_genres = sorted(genre_total.keys(), key=lambda x: genre_total[x], reverse=True)

    answer = []

    # 재생 수가 많은 장르부터 처리
    for genre in sorted_genres:
        songs = sorted(genre_songs[genre], key=lambda x: (-x[0], x[1]))
    # 앞에서 최대 2개까지 answer에 추가
        for i in range(min(2, len(songs))):
            answer.append(songs[i][1])

    return answer
