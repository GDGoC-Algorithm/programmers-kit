from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    # words 안의 단어를 방문했는지 체크
    visited = [False] * len(words)
    
    queue = deque()
    
    # 시작 단어, 현재까지의 변환 횟수
    queue.append((begin, 0))
    
    # 두 단어가 한 글자만 다른지 확인
    def can_change(word1, word2):
        diff = 0
        
        for a, b in zip(word1, word2):
            if a != b:
                diff += 1
        
        return diff == 1
    
    while queue:
        # 큐에서 현재 단어와 현재까지의 변환 횟수를 꺼냄
        current, count = queue.popleft()
        
        # 현재 단어가 target이면 정답
        if current == target:
            return count
        
        # words에 있는 모든 단어를 확인
        for i in range(len(words)):
            # 아직 방문하지 않은 단어이고, can_change면
            if not visited[i] and can_change(current, words[i]):
                visited[i] = True
                queue.append((words[i], count + 1))
    
    return 0
