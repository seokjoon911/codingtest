import sys
import math

def eratosthenes(n):
    sieve = [True] * (n + 1)  # 0~n까지의 숫자 리스트를 생성하고, 소수 여부를 저장할 리스트를 True로 초기화
    sieve[0] = False  # 0은 소수가 아니므로 False로 변경
    sieve[1] = False  # 1은 소수가 아니므로 False로 변경

    for i in range(2, int(math.sqrt(n)) + 1):
        if sieve[i] == True:  # i가 소수인 경우
            for j in range(i * 2, n + 1, i):  # i의 배수들을 False로 변경
                sieve[j] = False

    return sieve

sieve = eratosthenes(123456 * 2)  # 123456*2까지의 숫자들에 대한 소수 리스트를 생성

while True:
    n = int(sys.stdin.readline())
    if n == 0 :
        break
    cnt = 0
    for i in range(n+1, 2*n+1):
        if sieve[i]:  # i가 소수인 경우
            cnt += 1
    print(cnt)