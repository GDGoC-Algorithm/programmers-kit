from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    
    while prices:
        current_price = prices.popleft()
        sec = 0
        
        for next_price in prices:
            sec += 1
            if current_price > next_price:
                break
        
        answer.append(sec)
        
    return answer
