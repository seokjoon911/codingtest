def solution(board, k):
    row = len(board)
    col = len(board[0])
    total = 0
    
    for i in range(row):
        for j in range(col):
            if i + j <= k:
                total += board[i][j]
    
    return total