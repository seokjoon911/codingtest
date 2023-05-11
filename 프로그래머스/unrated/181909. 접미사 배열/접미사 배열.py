def solution(my_string):
    str_len = len(my_string)
    return sorted([my_string[idx:str_len] for idx in range(str_len)])
