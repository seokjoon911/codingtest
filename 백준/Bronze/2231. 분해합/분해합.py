N = int(input())
num = 0

for i in range(1, N + 1):
    tmp = i + sum(map(int,str(i)))
    
    if tmp == N:
        num = i
        break

print(num)