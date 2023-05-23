def solution(strArr):
    groups = {}  # 그룹별로 문자열 개수를 저장할 딕셔너리

    for string in strArr:
        length = len(string)
        if length in groups:
            groups[length] += 1
        else:
            groups[length] = 1

    max_count = max(groups.values())  # 그룹별 문자열 개수 중 최댓값

    return max_count