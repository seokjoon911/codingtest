import sys

T = int(sys.stdin.readline())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    result = A*B

    while B > 0:
        A, B = B, A % B

    print(result // A)