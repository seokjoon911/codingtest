def solution(n):
    arr = [[0] * n for _ in range(n)]
    move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    px, py, idx = 0, 0, 0
    npx, npy = 0, 0
    
    for i in range(1, n * n + 1):
        arr[px][py] = i
        
        npx = px + move[idx][0]
        npy = py + move[idx][1]
        
        if npy >= n or npx >= n or npy < 0 or npx < 0 or arr[npx][npy] != 0:
            idx = (idx + 1) % 4
            npx = px + move[idx][0]
            npy = py + move[idx][1]
        
        px = npx
        py = npy
    
    return arr