def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def solution(numbers):
    primes = set()
    cards = list(numbers)
    visited = [False] * len(cards)

    def make_number(current_str):
        if current_str:
            num = int(current_str)
            if is_prime(num):
                primes.add(num)

  
        for i in range(len(cards)):
            if not visited[i]:
                visited[i] = True  
                make_number(current_str + cards[i]) 
                visited[i] = False 

    make_number("") 
    return len(primes)
