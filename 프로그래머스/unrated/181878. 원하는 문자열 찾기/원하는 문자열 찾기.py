def solution(myString, pat):
    myString = myString.lower()  # 대소문자 구분을 없애기 위해 모두 소문자로 변환
    pat = pat.lower()
    if len(myString) < len(pat):  # myString의 길이가 pat보다 짧으면 0을 반환
        return 0
    for i in range(len(myString) - len(pat) + 1):
        if myString[i:i+len(pat)] == pat:  # myString의 부분 문자열이 pat과 같으면 1을 반환
            return 1
    return 0  # 부분 문자열 중 pat과 같은 문자열이 없으면 0을 반환