def solution(phone_book):
    # 1. 전화번호부를 사전순으로 정렬
    phone_book.sort()
    
    # 2. 리스트를 돌면서 현재 번호가 바로 다음 번호의 접두어인지 확인
    for i in range(len(phone_book) - 1):
        # 바로 뒤의 번호가 현재 번호로 시작한다면 접두어 관계임
        if phone_book[i+1].startswith(phone_book[i]):
            return False
            
    # 반복문이 끝날 때까지 발견되지 않으면 접두어가 없는 것
    return True
