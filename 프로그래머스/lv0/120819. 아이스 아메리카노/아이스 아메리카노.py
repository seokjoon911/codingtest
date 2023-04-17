def solution(money):
    cnt= money // 5500
    change = money % 5500
    answer = []
    answer.append(cnt)
    answer.append(change)
    return answer