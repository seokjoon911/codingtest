def solution(arr):
    length = len(arr)
    while length & (length - 1) != 0:  # 길이가 2의 거듭제곱인지 확인
        length += 1
    return arr + [0] * (length - len(arr))