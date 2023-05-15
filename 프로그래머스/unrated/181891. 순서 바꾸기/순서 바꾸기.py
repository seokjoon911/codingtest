def solution(num_list, n):
    return num_list[n:] + num_list[:n]  # n 번째 이후의 원소들과 n 번째까지의 원소들을 이어 붙여서 반환