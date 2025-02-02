import sys
from collections import deque

N = int(sys.stdin.readline())
Q = deque([])

for _ in range(N):
    C = sys.stdin.readline().split()
    if C[0] == 'push':
        Q.append(C[1])
    elif C[0] == 'pop':
        if len(Q) == 0:
            print(-1)
        else:
            print(Q.popleft())
    elif C[0] == 'size':
        print(len(Q))
    elif C[0] == 'empty':
        if len(Q) == 0:
            print(1)
        else:
            print(0)
    elif C[0] == 'front':
        if len(Q) == 0:
            print(-1)
        else:
            print(Q[0])
    elif C[0] == 'back':
        if len(Q) == 0:
            print(-1)
        else:
            print(Q[-1])