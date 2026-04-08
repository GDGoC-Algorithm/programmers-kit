from collections import deque

def solution(n, wires):
    # 전선을 하나씩 끊어보면서 개수 차이를 갱신하자
    
    answer = n
    
    for cut in range(len(wires)):
        graph = [[] for _ in range(n + 1)]
        
        for i, (a, b) in enumerate(wires):
            if i == cut: # 만약 cut번째 전선이면 제외
                continue
            graph[a].append(b)
            graph[b].append(a)

        # 1번 노드부터 연결된 송전탑 개수 세기
        # 일단 한 쪽 송전탑 개수만 세면 나머지는 n - count임
        visited = [False] * (n + 1)
        queue = deque([1])
        visited[1] = True
        count = 1

        while queue:
            now = queue.popleft()
            for next_node in graph[now]:
                if not visited[next_node]:
                    visited[next_node] = True
                    queue.append(next_node)
                    count += 1

        diff = abs(count - (n - count))
        answer = min(answer, diff)
    
    return answer
