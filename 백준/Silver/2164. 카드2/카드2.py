import sys
from collections import deque

N = int(sys.stdin.readline())
C = deque([i for i in range(1, N + 1)])

while len(C) > 1:
    # 첫 번째 요소를 제거 (버림)
    C.popleft()
    # 두 번째 요소를 제거하고, 그 값을 큐의 맨 뒤에 추가
    moved_card = C.popleft()
    C.append(moved_card)

# 마지막 남은 카드 출력
print(C[0])