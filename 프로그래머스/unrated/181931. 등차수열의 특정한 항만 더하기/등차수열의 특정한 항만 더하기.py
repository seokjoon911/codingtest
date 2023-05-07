def solution(a, d, included):
    arr = [a]
    for i in range(1, len(included)):
        arr.append(arr[i-1] + d)
    
    return sum([arr[i] for i in range(len(arr)) if included[i]]) if included else 0