from collections import deque

def solution(k, dungeons):
    answer = 0
    n = len(dungeons)
    
    queue = deque()
    queue.append((k, [False] * n, 0)) # 현재 피로도, 방문 여부, 방문 개수
    
    while queue:
        fatigue, visited, count = queue.popleft()
        answer = max(answer, count)
        
        for i in range(n):
            need, use = dungeons[i]
            
            # 아직 방문하지 않았고, 현재 피로도로 입장 가능하면
            if visited[i] is False and fatigue >= need:
                next_visited = visited[:]
                next_visited[i] = True
                queue.append((fatigue - use, next_visited, count + 1))
        
    return answer
