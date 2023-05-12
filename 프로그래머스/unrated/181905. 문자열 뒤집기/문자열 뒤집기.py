def solution(my_string, s, e):
    # 문자열의 일부를 슬라이싱하여 세 부분으로 나누고, 중간 부분을 뒤집은 후 이어붙임
    return my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]

