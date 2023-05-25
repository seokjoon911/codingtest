def solution(rank, attendance):
    answer = 0
    cnt = 0
    index = [0] * (len(rank) + 1)  # 등수별 인덱스를 저장할 리스트 초기화

    # 각 등수별로 인덱스 저장
    for i in range(len(rank)):
        index[rank[i]] = i

    for i in range(1, len(rank) + 1):
        num = index[i]  # 등수에 해당하는 인덱스 사용
        if attendance[num]:
            answer += num * 100 ** (2 - cnt)
            cnt += 1     
        if cnt == 3:
            break
    return answer
