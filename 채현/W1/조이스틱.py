def solution(name):
    answer = 0
    n = len(name)

    for ch in name:
        answer += min(ord(ch) - ord('A'), ord('Z') - ord(ch) + 1)
    
    move = n - 1
    for i in range(n):
        j = i + 1
        while j < n and name[j] == 'A':
            j += 1
        move = min(move, 2 * i + (n - j), i + 2 * (n - j))
    
    answer += move
    
    return answer
