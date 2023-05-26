def solution(s):
    if len(s) != 4 and len(s) != 6:  # 문자열의 길이가 4 또는 6이 아닐 경우
        return False
    for char in s:
        if not char.isdigit():  # 숫자가 아닌 문자가 포함되어 있을 경우
            return False
    return True