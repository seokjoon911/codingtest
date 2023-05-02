def solution(my_string, overwrite_string, s):
    my_str = list(my_string)
    my_str[s:s+len(overwrite_string)] = list(overwrite_string)
    return ''.join(my_str)