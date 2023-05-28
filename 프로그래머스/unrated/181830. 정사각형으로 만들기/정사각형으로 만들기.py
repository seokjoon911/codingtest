def solution(arr):
    row = len(arr)
    col = len(arr[0])

    if row > col:
        n = [0] * (row - col)
        return [a + n for a in arr]

    if col > row:
        for i in range(col - row):
            n = [0] * col
            arr.append(n)

    return arr