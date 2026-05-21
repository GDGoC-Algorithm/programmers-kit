import math

def solution(arrayA, arrayB):
    # arrayA의 모든 숫자의 최대공약수 구하기
    gcd_A = arrayA[0]
    for num in arrayA[1:]:
        gcd_A = math.gcd(gcd_A, num)
        
    # arrayB의 모든 숫자의 최대공약수 구하기
    gcd_B = arrayB[0]
    for num in arrayB[1:]:
        gcd_B = math.gcd(gcd_B, num)
        
    # gcd_A가 arrayB의 숫자를 하나도 나누지 못하는지 확인
    # 하나라도 나누어 떨어지면 후보에서 탈락(0으로 만듦)
    for num in arrayB:
        if num % gcd_A == 0:
            gcd_A = 0
            break  # 더 볼 필요 없으므로 탈락
            
    # gcd_B가 arrayA의 숫자를 하나도 나누지 못하는지 확인
    for num in arrayA:
        if num % gcd_B == 0:
            gcd_B = 0
            break  # 더 볼 필요 없으므로 탈락
            
    # 5. 둘 중 더 큰 값을 반환 (둘 다 탈락해서 0이면 0이 반환됨)
    return max(gcd_A, gcd_B)
