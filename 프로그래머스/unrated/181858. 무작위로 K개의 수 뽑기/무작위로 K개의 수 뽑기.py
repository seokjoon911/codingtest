def solution(arr, k):
    answer = []
    cnt = 0
    for num in arr:
        if num not in answer:
            answer.append(num)
            cnt += 1
            if cnt == k:
                break
    while cnt < k:
        answer.append(-1)
        cnt += 1
    return answer
