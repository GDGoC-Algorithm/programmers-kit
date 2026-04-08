def solution(n, wires):
    answer = n
    
    for i in range(len(wires)):
        sub_wires = wires[:i] + wires[i+1:]
        
        cluster = {wires[i][0]}
        
        for _ in range(len(sub_wires)):
            for v1, v2 in sub_wires:
                if v1 in cluster: cluster.add(v2)
                if v2 in cluster: cluster.add(v1)
        
        count = len(cluster)
        answer = min(answer, abs(count - (n - count)))
        
    return answer
