from collections import deque

def solution(priorities, location):
    waiting = deque()
    
    for index, priority in enumerate(priorities):
        waiting.append((priority, index))
    
    answer = 0
    
    while waiting:
        current_priority, current_index = waiting.popleft()
        
        if waiting and current_priority < max(priority for priority, index in waiting):
            waiting.append((current_priority, current_index))
        
        else:
            answer += 1
            
            if current_index == location:
                return answer
