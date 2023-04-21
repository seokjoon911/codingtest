import sys

N = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))

d= {} # 빈 딕셔너리 생성
for i in range(len(card)):
    d[card[i]] = 0  #card 리스트의 모든 요소들을 딕셔너리의 key로 설정하고, 각 key의 value를 0으로 초기화

for j in range(M):
    if check[j] not in d: # check[j]가 딕셔너리 d의 key로 없을 경우
        print(0, end=' ')
    else: # check[j]가 딕셔너리 d의 key로 있을 경우
        print(1, end=' ')