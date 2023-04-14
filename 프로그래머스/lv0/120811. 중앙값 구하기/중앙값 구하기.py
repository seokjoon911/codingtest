def solution(array):
    array.sort()
    center_idx = len(array)//2 
    return array[center_idx]