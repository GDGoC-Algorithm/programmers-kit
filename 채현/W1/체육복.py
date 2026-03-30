# 처음에는 단순히 lost 학생이 앞번호(i-1), 없으면 뒷번호(i+1)에게 체육복을 빌리는 방식으로 생각했다.
# 그런데 전체 테스트에서는 통과하지 못하는 케이스가 있었다.

# 문제를 다시 보니 여벌이 있는 학생도 도난당할 수 있어서,
# lost와 reserve에 동시에 포함된 학생을 먼저 처리하도록 수정했다.
# 하지만 이 경우에도 일부 케이스가 여전히 통과하지 않았다.

# 반복문으로 lost를 순회하면서 동시에 lost.remove()를 호출하고 있었는데
# 이렇게 되면 리스트가 순회 도중 변경되어 일부 원소를 건너뛸 수 있다.

# 그래서 lost를 직접 수정하지 않고, 실제로 체육복이 없는 학생만 new_lost에 따로 담아 처리하도록 바꿨다.

def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
            
    new_lost = []
    for x in lost:
        if x in reserve:
            reserve.remove(x)
        else:
            new_lost.append(x)

    lost = new_lost
    
    for i in lost:
        if (i - 1) in reserve:
            reserve.remove(i - 1)
        elif (i + 1) in reserve:
            reserve.remove(i + 1)
        else:
            n -= 1
            
    answer = n
    return answer
