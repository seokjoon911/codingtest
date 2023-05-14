def solution(arr, query):
    for i in range(len(query)):
        if i % 2 == 0:  # 짝수 인덱스일 때
            arr = arr[:query[i]+1]  # 해당 인덱스까지 슬라이싱하여 잘라냄
        else:  # 홀수 인덱스일 때
            arr = arr[query[i]:]  # 해당 인덱스부터 끝까지 슬라이싱하여 잘라냄
    return arr