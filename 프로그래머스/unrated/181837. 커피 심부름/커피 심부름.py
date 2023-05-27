def solution(order):
    answer = 0
    for drink in order:
        if "cafelatte" in drink:
            answer += 5000
        else:
            answer += 4500
    return answer