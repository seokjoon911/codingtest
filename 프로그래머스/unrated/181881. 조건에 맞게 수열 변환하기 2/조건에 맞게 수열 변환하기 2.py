def solution(arr):
    answer = 0
    count = 0
    before_arr = arr.copy()
    while count != len(arr):
        count = 0
        before_arr = arr.copy()
        for i in range(len(arr)):
            if arr[i] % 2 == 0 and arr[i] >= 50:
                arr[i] //= 2
            elif arr[i] % 2 != 0 and arr[i] < 50:
                arr[i] = arr[i] * 2 + 1
            if arr[i] == before_arr[i]:
                count += 1
        answer += 1
    
    return answer - 1