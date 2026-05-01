# 적용 알고리즘의 개념 
    # 스택
    # 아직 가격이 떨어지지 않은 시점들을 스택에 넣어두고, 현재 가격이 더 작아지는 순간 한 번에 처리하기

# 문제 풀이를 위한 접근 방식(or 개념) 설명
    # '가격이 아직 안 떨어진 시점'만 따로 관리하기
    # 현재 가격을 보면서, 스택에 있는 이전 가격보다 작아지는 순간 그 시점들의 기간을 확정

      # 가격이 유지되거나 오르면 스택에 쌓고
      # 가격이 떨어지면 떨어질 때까지 스택에서 꺼내며 정답 기록

# 기본 코드와 개선한 코드 비교
    # 스택에 인덱스를 저장해 한 번만 넣고 한 번만 뺌
    # O(n)

# 사용 라이브러리 정리
    # 리스트를 스택처럼 사용? 

def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []

    for i in range(n):
        while stack and prices[stack[-1]] > prices[i]:
            idx = stack.pop()
            answer[idx] = i - idx
        stack.append(i)

    while stack:
        idx = stack.pop()
        answer[idx] = n - 1 - idx

    return answer

