def solution(d, budget):
    d.sort()  # 예산을 오름차순으로 정렬
    count = 0  # 선택한 부서의 개수
    for cost in d:
        if budget >= cost:  # 예산이 물품 비용을 초과하지 않을 경우
            budget -= cost  # 예산에서 물품 비용을 차감
            count += 1  # 부서 개수 증가
        else:
            break  # 예산을 초과한 경우 더 이상 부서를 선택하지 않음
    return count