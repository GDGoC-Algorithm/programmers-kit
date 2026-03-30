def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2]) # 비용 오름차순
    link = set([costs[0][0]]) # 가장 적은 비용의 시작점

    while len(link) != n:
        for v in costs:
            if v[0] in link and v[1] in link:
                continue
            if v[0] in link or v[1] in link:
                link.update([v[0], v[1]])
                answer += v[2]
                break
                
    return answer
