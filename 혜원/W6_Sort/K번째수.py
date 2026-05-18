# 적용 알고리즘의 개념
    # 슬라이싱 + 정렬
    # 배열의 특정 구간을 자른 뒤 정렬해서 원하는 위치의 값을 찾는 방식

# 문제 풀이를 위한 접근 방식(개념) 설명
    # commands의 각 원소에는 i, j, k가 들어 있다.
    # 따라서 각 명령마다
    # 1. array에서 i번째부터 j번째까지 자르고
    # 2. 정렬한 뒤
    # 3. k번째 값을 answer에 넣으면 된다.

    # 슬라이싱
    # ** 주의) 문제는 1번부터 세지만 파이썬 인덱스는 0번부터 시작하므로, i-1부터 j까지 자를 것

# 사용 라이브러리 정리
    # 별도 라이브러리 없음
    # 슬라이싱과 sorted 사용

def solution(array, commands):
    answer = []

    for i, j, k in commands:
        # i번째부터 j번째까지 자르기
        arr = array[i - 1:j]

        # 정렬
        arr.sort()

        # k번째 값 넣기
        answer.append(arr[k - 1])

    return answer