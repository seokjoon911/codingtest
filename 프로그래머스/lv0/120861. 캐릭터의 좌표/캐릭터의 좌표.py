def solution(keyinput, board):
    x_boundary = board[0] // 2
    y_boundary = board[1] // 2
    result = [0,0]
    for i in keyinput:
        if i == "left" and result[0]-1 >= -(x_boundary):
            result[0]-=1
        elif i == "right" and result[0]+1 <= (x_boundary):
            result[0] += 1
        elif i == "up" and result[1] +1 <= (y_boundary):
            result[1] += 1
        elif i == "down" and result[1] -1 >= -(y_boundary):
            result[1] -= 1    
    return result