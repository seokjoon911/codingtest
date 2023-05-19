def solution(n):
    num = sorted(str(n), reverse=True)  # 각 자릿수를 문자열로 변환하여 정렬
    return int(''.join(num))  # 정렬된 자릿수를 문자열로 결합하고 정수로 변환하여 반환
