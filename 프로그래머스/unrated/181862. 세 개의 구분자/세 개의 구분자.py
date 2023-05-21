def solution(myStr):
    answer = []
    start = 0
    for i in range(len(myStr)):
        if myStr[i] in ['a', 'b', 'c']:
            if start != i:
                answer.append(myStr[start:i])
            start = i + 1
    if start < len(myStr):
        answer.append(myStr[start:])
    if not answer:
        answer = ["EMPTY"]
    return answer