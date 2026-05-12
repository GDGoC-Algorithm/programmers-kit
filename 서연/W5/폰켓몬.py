def solution(nums):
    # 1. 포켓몬 종류의 개수 구하기(set을 사용하면 중복 제거됨)
    unique_types = len(set(nums))
    
    # 2. 내가 가져갈 수 있는 최대 포켓몬 마리수 구하기
    max_pick = len(nums) // 2
    
    # 3. 종류의 개수가 아무리 많아도 max_pick보다 많이 가져갈 수는 없고,
    #    max_pick이 커도 종류가 적으면 그 종류만큼만 가져갈 수 있음.
    #    --> 따라서 두 값 중 더 작은 값 반환
    return min(unique_types, max_pick)
