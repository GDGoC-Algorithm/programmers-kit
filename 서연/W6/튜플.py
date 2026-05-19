def solution(s):
    s = s[2:-2].split("},{")
    s.sort(key=len)
    
    answer = []
    for item in s:
        numbers = list(map(int, item.split(",")))
        for num in numbers:
            if num not in answer:
                answer.append(num)
                break
                
    return answer
