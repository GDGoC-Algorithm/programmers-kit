# 적용 알고리즘의 개념
    # 큐 + 시뮬레이션
    # 다리 위 트럭들을 순서대로 관리하면서, 못 올라가면 다음 트럭이 나가는 시점으로 시간을 점프

# 문제 풀이를 위한 접근 방식(or 개념) 설명
    # 다리 위 상태를 관리하는 것이 중요
    # 리스트 + front 인덱스로 큐처럼 처리하기
      # 각 트럭에 대해
      # 현재 시간까지 다리를 지난 트럭은 제거하고,
      # 다음 트럭이 무게/길이 조건을 만족하면 올림
      # 못 올라가면 1초씩 늘리지 않고, 맨 앞 트럭이 나가는 시간으로 바로 이동

# 기본 코드와 개선한 코드 비교
    # O(n)


def solution(bridge_length, weight, truck_weights):
    on_bridge = []  # (나가는 시간, 트럭 무게)
    front = 0
    current_weight = 0
    time = 0

    for truck in truck_weights:
        while True:
            # 현재 시간까지 다리를 지난 트럭 제거
            while front < len(on_bridge) and on_bridge[front][0] <= time:
                current_weight -= on_bridge[front][1]
                front += 1

            # 다음 트럭을 올릴 수 있으면 올리기
            if len(on_bridge) - front < bridge_length and current_weight + truck <= weight:
                current_weight += truck
                on_bridge.append((time + bridge_length, truck))
                time += 1
                break
            else:
                # 못 올리면 맨 앞 트럭이 나가는 시간으로 점프
                time = on_bridge[front][0]

    return on_bridge[-1][0] + 1

