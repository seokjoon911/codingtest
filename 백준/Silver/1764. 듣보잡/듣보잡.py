import sys

N, M = map(int, sys.stdin.readline().split())
name1 = set()
name2 = set()

for _ in range(N):
    name1.add(sys.stdin.readline().rstrip())
for _ in range(M) :
    name2.add(sys.stdin.readline().rstrip())

name = sorted(list(name1 & name2))
print(len(name))

for i in name :
    print(i)