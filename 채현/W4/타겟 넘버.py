def solution(numbers, target):
    
    def dfs(index, total):
        if index == len(numbers):
            if total == target:
                return 1
            return 0
        
        # 현재 숫자를 더하는 경우의 수
        plus = dfs(index + 1, total + numbers[index])
        
        # 현재 숫자를 빼는 경우의 수
        minus = dfs(index + 1, total - numbers[index])
        
        return plus + minus
    
    return dfs(0, 0)
