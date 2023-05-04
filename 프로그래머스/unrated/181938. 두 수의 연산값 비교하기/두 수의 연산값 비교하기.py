def solution(a, b):
    atob = str(a) + str(b)
    ab2 = 2 * a * b
    return int(atob) if int(atob) >= ab2 else ab2