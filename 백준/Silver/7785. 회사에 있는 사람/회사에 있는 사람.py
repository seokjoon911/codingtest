import sys

n = int(sys.stdin.readline())
d = {}

for _ in range(n):
    p, c = sys.stdin.readline().split()
    if c == 'enter':
        d[p] = 'enter'
    else:
        if d[p] :
            del d[p]
            
for people in sorted(d, reverse=True):
    print(people)
