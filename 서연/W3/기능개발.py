import math

def solution(progresses, speeds):
    days_left = []
    for p, s in zip(progresses, speeds):
        day = math.ceil((100 - p) / s)
        days_left.append(day)
    
    answer = []
    current_day = days_left[0]
    count = 0
    
    for day in days_left:
        if day <= current_day:
            count += 1
        else:
            answer.append(count)
            current_day = day
            count = 1
            
    answer.append(count)
    
    return answer
