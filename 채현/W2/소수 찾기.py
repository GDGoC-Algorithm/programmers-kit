def solution(numbers):
    generated_numbers = set()

    # stack에는 (현재까지 만든 문자열, 사용 여부 리스트)를 저장
    stack = [("", [False] * len(numbers))]

    while stack:
        # 현재 상태 꺼내기
        current, visited = stack.pop()

        # 하나라도 만든 숫자가 있다면 set에 추가
        if current:
            generated_numbers.add(int(current))

        for i in range(len(numbers)):
            if not visited[i]:  
                new_visited = visited[:]   
                new_visited[i] = True      

                # 현재 숫자에 새로운 숫자를 붙여서 stack에 추가
                stack.append((current + numbers[i], new_visited))

    count = 0
    for num in generated_numbers:
        if is_prime(num):
            count += 1

    return count

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True
