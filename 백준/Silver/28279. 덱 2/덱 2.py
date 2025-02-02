import sys
from collections import deque

IN = sys.stdin.read().splitlines()
N = int(IN[0])
D = deque()
    
for line in IN[1:N+1]:
    op = line.split()
    if op[0] == '1':
        D.appendleft(int(op[1]))
    elif op[0] == '2':
        D.append(int(op[1]))
    elif op[0] == '3':
        print(D.popleft() if D else -1)
    elif op[0] == '4':
        print(D.pop() if D else -1)
    elif op[0] == '5':
        print(len(D))
    elif op[0] == '6':
        print(1 if not D else 0)
    elif op[0] == '7':
        print(D[0] if D else -1)
    elif op[0] == '8':
        print(D[-1] if D else -1)