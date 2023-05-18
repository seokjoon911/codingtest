def solution(myString):
    answer = ''
    
    for c in myString:
        if c.lower() == 'a':
            answer += 'A'
        else:
            answer += c.lower()
    
    return answer