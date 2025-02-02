import sys
from collections import deque

N = int(sys.stdin.readline())
D = deque(enumerate(map(int, sys.stdin.readline().split()), start=1))

for i in range(N):
    P = D.popleft()
    print(P[0], end=' ')
    if P[1] > 0:
        D.rotate(-(P[1] - 1))  # 왼쪽으로 (P[1] - 1)만큼 회전
    else:
        D.rotate(-P[1])  # 왼쪽으로 -P[1]만큼 회전