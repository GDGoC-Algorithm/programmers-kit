def solution(numbers):
    nums = [str(num) for num in numbers]
    
    nums.sort(key=lambda x: x * 4, reverse=True)
    
    answer = ''.join(nums)
    
    if answer[0] == '0':
        return '0'
    
    return answer
