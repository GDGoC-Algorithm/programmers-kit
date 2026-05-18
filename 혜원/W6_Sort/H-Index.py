# 적용 알고리즘의 개념
    # 정렬
    # 인용 횟수를 정렬한 뒤,
    # 현재 위치에서 "이상 인용된 논문 수"를 비교해서 H-Index를 찾는 방식

# 문제 풀이를 위한 접근 방식(개념) 설명
    # H-Index는 h번 이상 인용된 논문이 h편 이상 있어야 한다.
    # 따라서 인용 횟수를 큰 순서대로 정렬해서 보는 것이 편하다.


# 기본 코드와 개선한 코드 비교
    # 정렬 후 한 번만 확인
    # O(n log n)

# 사용 라이브러리 정리
    # 별도 라이브러리 없음
    # sort 사용

def solution(citations):
    # 인용 횟수를 내림차순 정렬
    citations.sort(reverse=True)

    answer = 0

    for i in range(len(citations)):
        # i + 1편의 논문이 i + 1회 이상 인용되었는지 확인
        if citations[i] >= i + 1:
            answer = i + 1

    return answer