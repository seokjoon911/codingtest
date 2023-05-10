import functools

def solution(a, b, c, d):
    dices = [a, b, c, d]
    num_frequency = {}
    for dice in dices:
        if dice in num_frequency:
            num_frequency[dice] += 1
        else:
            num_frequency[dice] = 1

    val_info = list(num_frequency.values())
    key_info = list(num_frequency.keys())

    count_val = max(val_info)
    if count_val == 4:
        return a * 1111
    elif count_val == 3:
        three_key = next(key for key in key_info if num_frequency[key] == 3)
        one_key = next(key for key in key_info if num_frequency[key] == 1)
        return (10 * int(three_key) + int(one_key)) ** 2
    elif count_val == 2:
        if len(key_info) == 2:
            if a == b:
                return (a + c) * abs(a - c)
            return (a + b) * abs(a - b)
        else:
            return functools.reduce(lambda acc, cur: acc * cur if num_frequency[cur] == 1 else acc, key_info, 1)
    else:
        return min(a, b, c, d)