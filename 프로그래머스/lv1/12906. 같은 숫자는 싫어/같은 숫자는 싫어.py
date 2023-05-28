def solution(arr):
    answer = []
    # 첫 번째 숫자를 결과 리스트에 추가
    answer.append(arr[0])
    # 이전 숫자와 현재 숫자를 비교하여 같지 않을 때만 결과 리스트에 추가
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            answer.append(arr[i])
    return answer