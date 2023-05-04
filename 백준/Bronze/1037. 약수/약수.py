import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a_max = max(a)
a_min = min(a)
print(a_max * a_min)