def solution(number, k):
    stack = []

    for i in number:
        while k > 0 and stack and stack[-1] < i:
            stack.pop()
            k -= 1
        stack.append(i)

    # 아직 k가 남아 있으면 뒤에서 제거
    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)
