def solution(n):
    # 자연수를 문자열로 변환하여 역순으로 정렬한 후, 각 숫자를 정수로 변환하여 리스트로 반환합니다.
    return list(map(int, str(n)[::-1]))