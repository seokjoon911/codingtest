def solution(number):
    total_sum = sum(int(digit) for digit in number)  # 각 자리 숫자의 합을 계산
    remainder = total_sum % 9  # 합을 9로 나눈 나머지를 계산
    return remainder
