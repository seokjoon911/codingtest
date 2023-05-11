def solution(my_strings, parts):
    result = ""
    for idx, cur in enumerate(my_strings):
        from_idx, to_idx = parts[idx]
        cur_slice = cur[from_idx:to_idx + 1]
        result += cur_slice
    return result