# 적용 알고리즘의 개념
    # 해시(set)
    # 모든 전화번호를 set에 넣어두고,
    # 각 전화번호의 앞부분(접두어)이 set 안에 있는지 확인함

# 문제 풀이를 위한 접근 방식(or 개념) 설명
    # 전화번호를 set에 저장해두고 찾기
    # 예를 들어 "1195524421"이 있으면
    # 앞에서부터 "1", "11", "119" 같은 접두어를 만들어 보고
    # 그 접두어가 set 안에 있으면 다른 번호의 접두어가 있다는 뜻으로 생각했다. 
    # -> 모든 번호를 서로 직접 비교하지 않아도 됨

# 기본 코드와 개선한 코드 비교
    # O(n * k)   (k=전화번호 길이, 최대 20)

def solution(phone_book):
    phone_set = set(phone_book)  # 모든 전화번호를 set에 저장

    # 각 전화번호를 하나씩 확인
    for phone in phone_book:
        prefix = ""

        # 자기 자신 전체 길이 전까지만 접두어 확인
        for i in range(len(phone) - 1):
            prefix += phone[i]

            # 접두어가 set 안에 있으면 False
            if prefix in phone_set:
                return False
            
    return True
