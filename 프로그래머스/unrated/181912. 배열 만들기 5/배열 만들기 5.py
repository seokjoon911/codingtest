def solution(intStrs, k, s, l):
    result = []
    for a in intStrs:
        sliceStr = a[s:s+l]
        num = int(sliceStr)
        if num > k:
            result.append(num)
    
    return result