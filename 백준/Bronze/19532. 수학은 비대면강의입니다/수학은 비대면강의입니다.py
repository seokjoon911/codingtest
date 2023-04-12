a, b, c, d, e, f = map(int, input().split())
var = []

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x + b*y == c and d*x + e*y == f:
            var = [x, y]
            break

for i in range(2):
    print(var[i], end=' ')