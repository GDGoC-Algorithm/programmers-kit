from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    queue = deque([(begin, 0)])
    visited = set()
    
    while queue:
        current, dist = queue.popleft()
        
        if current == target:
            return dist
        
        for word in words:
            if word not in visited:
                diff = sum(1 for a, b in zip(current, word) if a != b)
                if diff == 1:
                    visited.add(word)
                    queue.append((word, dist + 1))
                    
    return 0
