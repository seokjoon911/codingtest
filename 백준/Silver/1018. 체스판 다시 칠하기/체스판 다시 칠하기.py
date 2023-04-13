N, M = map(int, input().split())
color = []
cnt = []

for i in range(N) :
    color.append(input())
    
for a in range(N-7) : 
    for b in range(M-7) : #8*8로 자르기 위해, -7해준다
        w_index = 0 #흰색으로 시작
        b_index = 0 #검은색으로 시작
        for i in range(a, a+8) : #시작지점
            for j in range(b, b+8) : #시작지점
                if (i+j) % 2 == 0 : #짝수인 경우
                    if color[i][j] != 'W' : #W 아닐 경우
                        w_index += 1 #W 칠하는 갯수
                    if color[i][j] != 'B' : #B 아닐 경우
                        b_index += 1 #B 칠하는 갯수
                else : #홀수인 경우
                    if color[i][j] != 'W' : #W 아닐 경우
                        b_index += 1 #B 칠하는 갯수
                    if color[i][j] != 'B' : #B 아닐 경우
                        w_index += 1 #W 칠하는 갯수
        cnt.append(w_index) #W로 시작할 때 경우의 수
        cnt.append(b_index) #B로 시작할 때 경우의 수
print(min(cnt))    
