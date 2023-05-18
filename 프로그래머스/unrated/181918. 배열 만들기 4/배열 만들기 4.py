def solution(arr):
    stk = [] # 스택 초기화
    i = 0 # 인덱스 초기화
    
    while i < len(arr):
        if not stk: # 스택이 비어있으면, 현재 배열의 값 추가
            stk.append(arr[i])
            i += 1
        elif stk[-1] < arr[i]: # 현재 배열의 값이 스택의 마지막 값보다 크면, 스택에 추가
            stk.append(arr[i])
            i += 1
        else: # 현재 배열의 값이 스택의 마지막 값보다 작거나 같으면, 스택에서 마지막 값 삭제
            stk.pop()
    
    return stk