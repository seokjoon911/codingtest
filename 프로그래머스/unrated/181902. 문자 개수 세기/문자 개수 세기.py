def solution(my_string):
    result = [0] * 52  # 알파벳 개수를 저장할 길이 52의 리스트 생성

    for char in my_string:
        if 'A' <= char <= 'Z':  # 대문자인 경우
            idx = ord(char) - ord('A')  # 알파벳의 인덱스 계산
            result[idx] += 1
        elif 'a' <= char <= 'z':  # 소문자인 경우
            idx = ord(char) - ord('a') + 26  # 알파벳의 인덱스 계산
            result[idx] += 1

    return result