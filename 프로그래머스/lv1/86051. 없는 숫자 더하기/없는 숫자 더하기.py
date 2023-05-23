def solution(numbers):
    total = 45  # 0부터 9까지의 숫자의 합
    for num in numbers:
        total -= num
    return total