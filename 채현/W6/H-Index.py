def solution(citations):
    citations.sort(reverse=True)
    
    answer = 0
    
    for i in range(len(citations)):
        h = i + 1
        
        if citations[i] >= h:
            answer = h
        else:
            break
            
    return answer
