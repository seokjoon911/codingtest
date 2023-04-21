def solution(dot):
    answer = 0
    if 0 < dot[0] and 0 < dot[1] :
        answer = 1
    elif dot[0] < 0 and 0 < dot[1] :
        answer = 2
    elif dot[0] < 0 and dot[1] < 0 :
        answer = 3
    else :
        answer = 4
    return answer