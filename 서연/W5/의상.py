def solution(clothes):
    # 1. 의상 종류별로 개수를 세기 위한 딕셔너리
    clothes_dict = {}
    
    for name, kind in clothes:
        if kind in clothes_dict:
            clothes_dict[kind] += 1
        else:
            clothes_dict[kind] = 1
            
    # 2. 모든 종류의 (개수 + 1)을 곱해주기
    answer = 1
    for count in clothes_dict.values():
        answer *= (count + 1)
        
    # 3. 아무것도 입지 않은 경우 1가지를 빼고 반환
    return answer - 1
