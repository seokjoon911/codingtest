def solution(n):
    result = []
    if n % 2 == 0:
        for i in range(n, 0, -1):
            if i % 2 == 0:
                result.append(i)
        return sum([x**2 for x in result])
    else:
        for i in range(n, 0, -1):
            if i % 2 == 1:
                result.append(i)
        return sum(result)