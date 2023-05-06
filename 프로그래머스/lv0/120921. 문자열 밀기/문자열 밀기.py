from collections import deque

def solution(A, B):
    ad = deque(A)
    bd = deque(B)
    for i in range(len(A)):
            a = ad.pop()
            ad.appendleft(a)
            if ad == bd:
                if i == len(A) - 1:
                    return 0
                return i+1
    return -1