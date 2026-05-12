# 적용 알고리즘의 개념
    # 해시(딕셔너리) + 경우의 수
    # 옷 이름이 아니라 "종류별 개수"를 세고
    # 각 종류에서 입는 경우 / 안 입는 경우를 계산해서 곱

# 문제 풀이를 위한 접근 방식(or 개념) 설명
    # 실제 조합을 만들 필요 없이 각 종류별 옷 개수만 알면 경우의 수를 바로 구할 수 있다.

    # 예를 들어 모자가 2개 있으면
    # 모자1, 모자2, 안 입음 -> 총 3가지 선택이 가능함
    # 안경이 1개 있으면
    # 안경1, 안 입음 -> 총 2가지 선택이 가능함

    # 이렇게 각 종류의 선택 경우를 모두 곱하면 전체 조합 수가 나옴
    # 단, 아무것도 안 입는 경우는 제외해야 하므로 마지막에 1을 빼기 


def solution(clothes):
    clothes_dict = {}  # 종류별 옷 개수 저장

    # 옷 종류별 개수 세기
    for name, kind in clothes:
        if kind in clothes_dict:
            clothes_dict[kind] += 1
        else:
            clothes_dict[kind] = 1

    answer = 1

    # 각 종류마다 "안 입는 경우" 1개를 더해서 곱하기
    for count in clothes_dict.values():
        answer *= (count + 1)

    # 아무것도 안 입는 경우 1개 제외
    return answer - 1
