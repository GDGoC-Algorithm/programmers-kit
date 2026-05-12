def solution(participant, completion):
    hash_dict = {}
    
    # 1. 모든 참가자를 딕셔너리에 넣고 카운트
    for name in participant:
        if name in hash_dict:
            hash_dict[name] += 1
        else:
            hash_dict[name] = 1
            
    # 2. 완주한 사람들은 딕셔너리 값에서 1을 빼기
    for name in completion:
        hash_dict[name] -= 1
        
    # 3. 값이 0이 아닌(1인) 사람이 완주하지 못한 사람임
    for name in hash_dict:
        if hash_dict[name] > 0:
            return name
