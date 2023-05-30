def solution(n):
    # n을 3진법으로 변환
    ternary = []
    while n > 0:
        n, remainder = divmod(n, 3)
        ternary.append(remainder)
    
    # 3진법을 뒤집고 10진법으로 변환
    answer = 0
    power = len(ternary) - 1
    for digit in ternary:
        answer += digit * (3 ** power)
        power -= 1
    
    return answer