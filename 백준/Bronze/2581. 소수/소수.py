N = int(input())
M = int(input())
nums = []
for i in range(N, M+1) :
    check = 0
    if i == 1: #1은 소수가 아니므로 예외처리
        continue
    for j in range(2, i):
        if i % j == 0:
            check = 1
    if check == 0:
        nums.append(i)
        
if(len(nums) > 0) :
    print(sum(nums))
    print(min(nums))
else :
    print(-1)