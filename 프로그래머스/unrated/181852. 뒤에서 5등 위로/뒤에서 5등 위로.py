def solution(num_list):
    sorted_list = sorted(num_list)  # num_list를 오름차순으로 정렬
    answer = sorted_list[5:]  # 5번째 인덱스부터 끝까지의 수 선택
    return answer