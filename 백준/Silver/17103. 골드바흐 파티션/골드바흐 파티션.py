import sys

# 테스트 케이스 수 입력
t = int(sys.stdin.readline())

# 0~1000000까지의 숫자 리스트를 생성하고, 소수 여부를 저장할 리스트를 True로 초기화
arr = [True for _ in range(1000001)]

# 에라토스테네스의 체 알고리즘을 이용하여 소수 구하기
for i in range(2, 1001):
    if arr[i]:
        for j in range(i * 2, 1000001, i):  # i의 배수들을 False로 변경
            arr[j] = False

# 각 테스트 케이스마다 소수 쌍의 개수 구하기
for _ in range(t):
    result = 0
    n = int(sys.stdin.readline().rstrip())

    for i in range(2, n // 2 + 1):
        if arr[i] and arr[n - i]:  # i와 n-i가 모두 소수인 경우
            result += 1
    
    # 소수 쌍의 개수 출력
    print(result)
