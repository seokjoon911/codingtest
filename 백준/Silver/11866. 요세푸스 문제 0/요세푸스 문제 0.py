import sys
from collections import deque

# 입력 처리
N, K = map(int, sys.stdin.readline().split())
deq = deque([i for i in range(1, N + 1)])

res = []
while len(deq) != 0:
    for _ in range(K - 1):
        # K-1번째 노드까지 deq 맨 뒤로 이동
        deq.append(deq.popleft())
    # K번째 노드 삭제 후 결과 배열에 추가
    res.append(str(deq.popleft()))

# 결과 출력
print('<' + ', '.join(res) + '>')