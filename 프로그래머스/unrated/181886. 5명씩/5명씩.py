def solution(names):
    answer = []
    group_count = (len(names) + 4) // 5  # 그룹의 개수
    
    for i in range(group_count):
        group = names[i*5 : (i+1)*5]  # 5명씩 묶은 그룹
        answer.append(group[0])  # 가장 앞에 있는 사람의 이름을 결과 리스트에 추가
    
    return answer
