def solution(start, end):
    result = []  # 숫자를 저장할 빈 리스트 생성
    for i in range(start, end - 1, -1):
        # start부터 end까지 (포함) 1씩 감소하면서 반복합니다.
        # end - 1을 사용하여 end 값을 결과에 포함시킵니다.
        # -1의 스텝 크기는 숫자가 감소함을 보장합니다.
        result.append(i)  # 현재 숫자를 결과 리스트에 추가합니다.
    return result  # 최종 결과 리스트를 반환합니다.
