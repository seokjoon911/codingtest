def solution(myString, pat):
    answer = myString.replace("A", "x").replace("B", "A").replace("x", "B")
    return 1 if pat in answer else 0
