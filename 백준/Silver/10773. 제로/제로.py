import sys

k = int(sys.stdin.readline())
n = []
for i in range(k):
    num = int(sys.stdin.readline())
    if num == 0:
        n.pop()
    else:
        n.append(num)
print(sum(n))