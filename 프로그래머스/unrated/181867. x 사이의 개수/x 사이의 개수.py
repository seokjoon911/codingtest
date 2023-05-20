def solution(myString):
    answer = []
    cnt = 0
    for char in myString:
        if char == 'x':
            answer.append(cnt)
            cnt = 0
        else:
            cnt += 1
    answer.append(cnt)
    return answer