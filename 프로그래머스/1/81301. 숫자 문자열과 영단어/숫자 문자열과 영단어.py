def solution(s):
    arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in arr:
        if i in s:
            idx = str(arr.index(i)) 
            s = s.replace(i, idx)
    answer = int(s)
    return answer