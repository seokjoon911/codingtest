def solution(a, b, c):
    answer = 0
    one, two, three = (a + b + c), (a**2 + b**2 + c**2), (a**3 + b**3 + c**3)
    if a == b and b == c :
        answer = one * two * three
    elif a == b or b == c or a == c:
        answer = one * two
    else:
        answer = one
    return answer