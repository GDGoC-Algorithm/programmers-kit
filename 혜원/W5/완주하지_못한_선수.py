# 적용 알고리즘의 개념
    # 해시(딕셔너리)
    # 사람 이름별로 몇 명 있는지 세어서 완주한 사람 수를 빼면 완주하지 못한 사람을 찾을 수 있다.

# 문제 풀이를 위한 접근 방식(or 개념) 설명
    # 처음에는 participant에 있고 completion에 없는 이름을 찾으면 되겠다고 생각할 수 있음
    # 그런데 이 문제는 동명이인이 있을 수 있어서
    # 단순히 이름이 있는지 없는지만 보면 안 됨

    # 그래서 이름별 인원 수를 세는 방식으로 생각
    # participant에서 이름이 나오면 +1
    # completion에서 이름이 나오면 -1
    # 마지막에 값이 1 남아 있는 이름이 완주하지 못한 선수임

# 기본 코드와 개선한 코드 비교
    # 단순히 리스트에서 remove 하거나 비교하면 비효율적
    # 딕셔너리로 개수를 세면 빠르게 해결 가능
    # O(n)


def solution(participant, completion):
    players = {}  # 이름별 참가 인원 수 저장

    # 참가자 이름 개수 세기
    for name in participant:
        if name in players:
            players[name] += 1
        else:
            players[name] = 1

    # 완주한 사람은 1명씩 빼기
    for name in completion:
        players[name] -= 1

    # 1이 남아 있는 사람이 완주하지 못한 선수
    for name in players:
        if players[name] > 0:
            return name
