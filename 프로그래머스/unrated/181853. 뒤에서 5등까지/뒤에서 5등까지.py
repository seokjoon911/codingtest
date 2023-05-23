def solution(num_list):
    sorted_list = sorted(num_list)  # num_list를 오름차순으로 정렬
    answer = sorted_list[:5]  # 앞에서부터 5개의 수 선택
    return answer