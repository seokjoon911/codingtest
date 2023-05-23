def solution(arr, n):
    length = len(arr)
    answer = []

    for i in range(length):
        if length % 2 == 0:  # arr의 길이가 짝수인 경우
            if i % 2 != 0:
                answer.append(arr[i] + n)
            else:
                answer.append(arr[i])
        else:  # arr의 길이가 홀수인 경우
            if i % 2 == 0:
                answer.append(arr[i] + n)
            else:
                answer.append(arr[i])

    return answer