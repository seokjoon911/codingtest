def solution(my_string, index_list):
    result = ''
    for index in index_list:
        result += my_string[index]
    return result
