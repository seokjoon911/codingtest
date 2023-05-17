def solution(s):
    s = s.lower()  # 대소문자 구분을 없애기 위해 모두 소문자로 변환
    count_p = s.count('p')  # 'p'의 개수 세기
    count_y = s.count('y')  # 'y'의 개수 세기
    return count_p == count_y  # 'p'의 개수와 'y'의 개수를 비교하여 True 또는 False 반환
