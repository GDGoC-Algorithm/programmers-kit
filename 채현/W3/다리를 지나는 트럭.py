from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    
    waiting_trucks = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    current_weight = 0
    
    while bridge:
        time += 1
        
        # 다리에서 맨 앞 위치가 빠짐
        current_weight -= bridge.popleft()
        
        # 아직 기다리는 트럭이 있다면
        if waiting_trucks:
            # 다음 트럭이 올라갈 수 있나?
            if current_weight + waiting_trucks[0] <= weight:
                truck = waiting_trucks.popleft()
                bridge.append(truck)
                current_weight += truck
            else:
                # 못 올라가면 빈 칸 추가
                bridge.append(0)
    
    return time
