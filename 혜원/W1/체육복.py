def solution(n, lost, reserve):
    lost_set = set(lost) #도난당한 학생 목록
    reserve_set = set(reserve) #여벌 체육복이 있는 학생 목록
    
    both = lost_set & reserve_set #교집합
    lost_set -= both
    reserve_set -= both
    
    for student in sorted(reserve_set):
        if student -1 in lost_set: #앞번호 학생이 체육복이 없으면 먼저 빌려줌
            lost_set.remove(student-1) #받았으니까 제거 
        elif student +1 in lost_set: #앞번호 학생이 없으면 뒷번호 학생에게 빌려줌
            lost_set.remove(student+1)
            
    return n-len(lost_set) #전체 - 끝까지 체육복을 못 빌린 학생 수
