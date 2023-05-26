def solution(price, money, count):
    total = price * (count * (count + 1)) // 2  # 놀이기구의 총 이용 금액 계산
    if total <= money:  # 가진 금액으로 모자라지 않을 경우
        return 0
    else:  # 가진 금액으로 모자랄 경우
        return total - money
