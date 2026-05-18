# 적용 알고리즘의 개념
    # 정규표현식 + 정렬
    # 파일명에서 NUMBER를 먼저 뽑아 정렬하고,
    # 그 다음 HEAD를 기준으로 다시 정렬하는 방식

# 문제 풀이를 위한 접근 방식(개념) 설명
    # 정규표현식을 이용해서
    # 숫자 부분(NUMBER)과 문자 부분(HEAD)을 쉽게 구할 수 있다.

    # 1. 먼저 NUMBER 기준으로 정렬하고,
    # 2. 그 다음 HEAD 기준으로 다시 정렬
    # 3. 파이썬의 sorted는 안정 정렬이기 때문에, HEAD가 같은 경우 앞에서 정렬한 NUMBER 순서가 그대로 유지된다.

# 기본 코드와 개선한 코드 비교
    # 직접 HEAD와 NUMBER를 나누는 방법도 가능하지만,
    # 이 코드는 re를 사용해서 더 짧고 간단하게 구현한 풀이이다. 
    # O(n log n)

# 사용 라이브러리 정리
    # re.findall(r'\d+', file)[0]
        # 파일명에서 처음 나오는 숫자 부분 추출
    # re.split(r'\d+', file.lower())[0]
        # 숫자를 기준으로 나눠서 HEAD 부분 추출
        # lower()를 사용해서 대소문자 구분 없이 비교

import re

def solution(files):
    # 먼저 NUMBER 기준으로 정렬
    arr = sorted(files, key=lambda file: int(re.findall(r'\d+', file)[0]))

    # 그 다음 HEAD 기준으로 정렬
    arr = sorted(arr, key=lambda file: re.split(r'\d+', file.lower())[0])

    return arr