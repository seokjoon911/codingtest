import sys

N  = int(sys.stdin.readline())
arr = []

for i in range(N) :
    x, y = map(int, sys.stdin.readline().split())
    arr.append([y, x]) 
               
arr.sort() 
               
for i in range(N) :
    print(arr[i][1], arr[i][0])
    