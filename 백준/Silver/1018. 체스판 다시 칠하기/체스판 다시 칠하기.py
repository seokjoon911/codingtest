N, M = map(int, input().split())
color = []
cnt = []

for i in range(N) :
    color.append(input())
    
for a in range(N-7) :
    for b in range(M-7) :
        w_index = 0
        b_index = 0
        for i in range(a, a+8) :
            for j in range(b, b+8) :
                if (i+j) % 2 == 0 :
                    if color[i][j] != 'W' :
                        w_index += 1
                    if color[i][j] != 'B' :
                        b_index += 1
                else :
                    if color[i][j] != 'W' :
                        b_index += 1
                    if color[i][j] != 'B' :
                        w_index += 1
        cnt.append(w_index)
        cnt.append(b_index)
print(min(cnt))
        