def solution(t, p):
    cnt = 0  # 작거나 같은 부분문자열의 개수를 세기 위한 변수

    for i in range(len(t) - len(p) + 1):
        sub_str = t[i:i+len(p)]  # 길이가 p와 같은 부분문자열 추출
        if sub_str <= p:  # 부분문자열이 p보다 작거나 같은지 비교
            cnt += 1

    return cnt