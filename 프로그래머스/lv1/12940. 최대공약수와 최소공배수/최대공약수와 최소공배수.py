def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def solution(n, m):
    answer = gcd(n, m)
    return [answer, int(n * m / answer)]