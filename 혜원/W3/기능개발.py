# 적용 알고리즘의 개념
    # 시뮬레이션 + 그리디
    # 각 기능이 완료되는 날짜를 먼저 구한 뒤,
    # 앞 기능의 배포일 기준으로 함께 배포할 수 있는 기능들을 묶음

# 문제 풀이를 위한 접근 방식(or 개념) 설명
    # 뒤 기능이 먼저 끝나도 앞 기능이 배포될 떄 같이 나가기 때문에, 각 기능이 완료되기까지 걸리는 일수를 먼저 계산하기 
      # 완료일을 앞에서부터 확인하면서,
      # 현재 배포 기준일보다 작거나 같으면 함께 배포 | 더 크면 새로운 배포 묶음을 시작

# 기본 코드와 개선한 코드 비교
    # O(n)

# 사용 라이브러리 정리
    # 완료일 계산 -> 올림 처리
      # (남은 작업량 + 속도 - 1) // 속도 사용

def solution(progresses, speeds):
    days = []
    
    for p, s in zip(progresses, speeds):
        days.append((100 - p + s - 1) // s)

    answer = []
    current = days[0]
    count = 1

    for i in range(1, len(days)):
        if days[i] <= current:
            count += 1
        else:
            answer.append(count)
            current = days[i]
            count = 1

    answer.append(count)
    return answer

