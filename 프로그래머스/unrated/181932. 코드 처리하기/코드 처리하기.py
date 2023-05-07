def solution(code):
    mode = 0
    result = ""
    for idx, cur in enumerate(code):
        if mode:
            if cur != '1' and idx % 2 == 1:
                result += cur
            if cur == '1':
                mode = 0
        else:
            if cur != '1' and idx % 2 == 0:
                result += cur
            if cur == '1':
                mode = 1

    return result if result != "" else "EMPTY"