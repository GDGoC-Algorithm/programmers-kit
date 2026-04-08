def solution(brown, yellow):
    n = brown + yellow
    
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            h = i
            w = n // i

            if (w - 2) * (h - 2) == yellow:
                return [w, h]
    

# brown + yellow 는 전체 칸수 (어차피 가로 세로는 전체 칸수의 약수쌍밖에 안됨)
# yellow는 (w - 2) * (h - 2)
