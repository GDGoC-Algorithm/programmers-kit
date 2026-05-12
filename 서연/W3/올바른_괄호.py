def solution(s):
    count = 0
    
    for bracket in s:
        if bracket == '(':
            count += 1
        else: # bracket == ')'인 경우
            count -= 1
            
        if count < 0:
            return False
            
    return count == 0
