def solution(s):
    # 바깥 {{ }} 제거하고, 집합 단위로 나누기
    groups = s[2:-2].split("},{")
    
    # 각 집합을 숫자 리스트로 바꾸기
    tuples = []
    for group in groups:
        nums = group.split(",")
        nums = [int(num) for num in nums]
        tuples.append(nums)
    
    # 집합 길이가 짧은 순서대로 정렬
    tuples.sort(key=lambda x: len(x))
    
    answer = []
    
    # 앞에서부터 보면서 answer에 없는 숫자만 추가
    for nums in tuples:
        for num in nums:
            if num not in answer:
                answer.append(num)
    
    return answer
