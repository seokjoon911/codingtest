def solution(numLog):
    control = ''
    n = numLog[0]
    for i in range(1, len(numLog)):
        diff = numLog[i] - numLog[i-1]
        if diff == 1:
            control += 'w'
            n += 1
        elif diff == -1:
            control += 's'
            n -= 1
        elif diff == 10:
            control += 'd'
            n += 10
        elif diff == -10:
            control += 'a'
            n -= 10
    return control