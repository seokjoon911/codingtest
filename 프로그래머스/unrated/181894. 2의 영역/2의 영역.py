def solution(arr):
    firstIndex = -1  # 첫 번째로 나타나는 2의 인덱스
    lastIndex = -1  # 마지막으로 나타나는 2의 인덱스

    # 첫 번째로 나타나는 2의 인덱스 찾기
    for i in range(len(arr)):
        if arr[i] == 2:
            firstIndex = i
            break

    # 첫 번째로 나타나는 2의 인덱스가 존재하는 경우
    if firstIndex != -1:
        # 마지막으로 나타나는 2의 인덱스 찾기
        for i in range(firstIndex, len(arr)):
            if arr[i] == 2:
                lastIndex = i

    result = []  # 결과를 저장할 리스트

    # 2가 존재하지 않는 경우
    if firstIndex == -1:
        result.append(-1)  # -1을 결과 리스트에 추가
    # 2가 한 번만 나타나는 경우
    elif firstIndex == lastIndex:
        result.append(2)  # 2를 결과 리스트에 추가
    # 2가 여러 번 나타나는 경우
    else:
        result = arr[firstIndex:lastIndex+1]  # 해당 구간을 결과 리스트에 저장

    return result