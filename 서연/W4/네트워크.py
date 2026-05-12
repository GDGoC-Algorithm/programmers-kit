def solution(n, computers):
    def dfs(node):
        visited[node] = True
        for neighbor, connected in enumerate(computers[node]):
            if connected and not visited[neighbor]:
                dfs(neighbor)
    
    visited = [False] * n
    answer = 0
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
            
    return answer
