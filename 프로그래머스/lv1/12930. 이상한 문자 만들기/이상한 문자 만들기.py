def solution(s):
    words = s.split(" ")  # 문자열을 공백을 기준으로 단어로 분리
    answer = []
    
    for word in words:
        converted = ""
        for i in range(len(word)):
            if i % 2 == 0:
                converted += word[i].upper()  # 짝수 인덱스는 대문자로 변환
            else:
                converted += word[i].lower()  # 홀수 인덱스는 소문자로 변환
        answer.append(converted)
    
    return " ".join(answer)  # 변환된 단어들을 공백으로 연결하여 문자열로 반환
