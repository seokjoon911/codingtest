def solution(phone_number):
    ph_len = len(phone_number)
    return '*' * (ph_len - 4) + phone_number[-4:]