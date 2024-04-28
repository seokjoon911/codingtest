from itertools import combinations

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    comb = list(combinations(nums, 3)) 

    for temp in comb:  
        if is_prime(sum(temp)):
            answer += 1

    return answer