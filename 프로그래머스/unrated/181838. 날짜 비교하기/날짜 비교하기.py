def solution(date1, date2):
    if date1[0] < date2[0]:  # year 비교
        return 1
    elif date1[0] > date2[0]:  # year 비교
        return 0
    elif date1[1] < date2[1]:  # month 비교
        return 1
    elif date1[1] > date2[1]:  # month 비교
        return 0
    elif date1[2] < date2[2]:  # day 비교
        return 1
    else:
        return 0