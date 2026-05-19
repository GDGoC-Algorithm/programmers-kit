def solution(array, commands):
    answer = []
    
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        
        sliced_array = array[i-1:j]
        sliced_array.sort()
        
        target_number = sliced_array[k-1]
        answer.append(target_number)
        
    return answer
