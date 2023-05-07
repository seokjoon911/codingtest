def solution(num_list):
    odd = ''.join(map(str, [n for n in num_list if n%2==1]))
    even = ''.join(map(str, [n for n in num_list if n%2==0]))
    return int(odd) + int(even)