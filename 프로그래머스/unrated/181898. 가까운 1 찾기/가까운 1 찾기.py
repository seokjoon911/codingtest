def solution(arr, idx):
    for i in range(idx, len(arr)):
        cur = arr[i]
        if cur == 1:
            return i
    return -1