from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    field = [[-1] * 102 for _ in range(102)]
    
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, r)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = 0
                elif field[i][j] != 0:
                    field[i][j] = 1
                    
    cx, cy, ix, iy = characterX * 2, characterY * 2, itemX * 2, itemY * 2
    
    queue = deque([(cx, cy)])
    visited = [[1] * 102 for _ in range(102)]
    visited[cx][cy] = 0
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        
        if x == ix and y == iy:
            return visited[x][y] // 2
            
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if field[nx][ny] == 1 and visited[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
