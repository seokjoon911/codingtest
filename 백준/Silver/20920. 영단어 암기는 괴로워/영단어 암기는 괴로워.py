import sys

n, m = map(int, sys.stdin.readline().split())
d = {}
for _ in range(n) :
    word = sys.stdin.readline().rstrip()
    if len(word) < m :
        continue
    if d.get(word) :
        d[word][0] += 1
    else :
        d[word] = [1, len(word), word]
ans = sorted(d.items(), key= lambda x: (-x[1][0], -x[1][1], x[1][2]))

for a in ans :
    print(a[0])