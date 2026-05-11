def solution(clothes):
    dic = {}

    for name, kind in clothes:
        if kind in dic:
            dic[kind] += 1
        else:
            dic[kind] = 1

    answer = 1

    # 각 종류마다 "입지 않는 경우"를 포함해서 + 1
    for kind in dic:
        answer *= (dic[kind] + 1)

    # 아무것도 입지 않는 경우 1개 제외
    return answer - 1
