import sys

input = sys.stdin.readline

n, m = map(int, input().split())
pk_id = {}
pk_name = {}

for i in range(1, n+1):
    pokemon = input().rstrip()
    pk_id[i] = pokemon
    pk_name[pokemon] = i

for _ in range(m):
    x = input().rstrip()
    if x.isdigit(): #숫자판별
        print(pk_id[int(x)])
    else:
        print(pk_name[x])