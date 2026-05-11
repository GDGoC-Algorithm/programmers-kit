from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    # 아래, 위, 오른쪽, 왼쪽
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    queue = deque()
    
    # 시작 위치
    queue.append((0, 0))
    
    # 시작 칸의 거리는 이미 1로 되어 있음
    # maps[x][y] 자체에 "시작점부터 여기까지의 거리"를 저장할 것
    
    while queue:
        # 현재 위치 꺼내기
        x, y = queue.popleft()
        
        # 상하좌우 4방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 맵 범위를 벗어나면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            # 벽이면 이동 불가
            if maps[nx][ny] == 0:
                continue
            
            # 아직 방문하지 않은 길이면 이동
            if maps[nx][ny] == 1:
                # 다음 칸까지의 거리 = 현재 칸까지의 거리 + 1
                maps[nx][ny] = maps[x][y] + 1
                
                queue.append((nx, ny))
    
    # 도착 지점의 값 확인
    answer = maps[n - 1][m - 1]
    
    # 도착 지점이 여전히 1이면 도달하지 못한 것
    if answer == 1:
        return -1
    
    return answer
