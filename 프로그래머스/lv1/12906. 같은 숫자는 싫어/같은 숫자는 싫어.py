def solution(arr):
    answer = [arr[0]]  # 첫 번째 원소를 answer에 추가
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:  # 현재 원소와 이전 원소가 다를 경우에만 추가
            answer.append(arr[i])
    return answer