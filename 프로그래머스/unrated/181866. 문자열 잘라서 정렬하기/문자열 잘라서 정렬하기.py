def solution(myString):
    answer = myString.split('x')
    answer = sorted(filter(lambda x: x != '', answer))
    return answer