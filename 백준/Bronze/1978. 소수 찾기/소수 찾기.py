N = int(input())
nums = list(map(int, input().split()))
cnt = 0

for i in nums:
    check = 0
    if i == 1: #1은 소수가 아니므로 예외처리
        continue
    for j in range(2, i):
        if i % j == 0:
            check = 1
    if check == 0:
        cnt += 1
print(cnt)