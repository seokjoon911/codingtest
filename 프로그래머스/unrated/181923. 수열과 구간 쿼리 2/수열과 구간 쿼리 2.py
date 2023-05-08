def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        tmp = sorted([v for i, v in enumerate(arr) if s <= i <= e and v > k])
        answer.append(tmp[0] if tmp else -1)
    return answer