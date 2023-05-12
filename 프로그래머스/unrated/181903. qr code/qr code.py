def solution(q, r, code):
    result = ""  # 결과를 저장할 빈 문자열 생성

    # 문자열 code의 각 인덱스를 순회하면서 처리
    for i in range(len(code)):
        if i % q == r:  # 현재 인덱스를 q로 나눈 나머지가 r과 일치하는지 확인
            result += code[i]  # 일치하는 경우 해당 인덱스의 문자를 결과 문자열에 추가

    return result  # 결과 문자열 반환
