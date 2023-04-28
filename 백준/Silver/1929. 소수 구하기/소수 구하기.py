import sys
import math
m, n=map(int, sys.stdin.readline().split())

for i in range(m,n+1) :
    if i == 1 :
        continue
    for j in range(2, int(math.sqrt(i))+1) :  # i의 약수를 구하기 위해 2부터 i의 제곱근까지 반복한다.
        if i % j==0:           # 약수가 존재하므로 소수가 아님
            break            # 더이상 검사할 필요가 없으므로 멈춤
    else:
        print(i)             # 소수인 경우 출력한다.
