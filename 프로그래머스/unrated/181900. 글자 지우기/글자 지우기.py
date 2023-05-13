def solution(my_string, indices):
    result = ""  # 결과를 저장할 빈 문자열
    for i in range(len(my_string)):
        if i not in indices:  # 현재 인덱스가 indices에 포함되지 않으면
            result += my_string[i]  # 해당 글자를 결과 문자열에 추가
    return result