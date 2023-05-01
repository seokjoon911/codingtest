import sys
import math

# 입력값 n을 sys.stdin.readline()으로 받음
n = int(sys.stdin.readline())

# 초기값 a를 1로 설정
a = 1

# 2부터 n의 제곱근까지 반복문 실행
for i in range(2, int(math.sqrt(n))+1):
    a += 1

# a 출력
print(a)