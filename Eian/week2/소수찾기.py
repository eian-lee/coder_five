#!/usr/bin/env python3

from itertools import permutations

def is_prime(n):
    n = int(n)
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 3:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2): # odd numbers
        if n % i == 0:
            return False
    else:
        return True


def solution(numbers):
    nums = set()
    for permuation in permutations(numbers):
        string = ""
        for num in permuation:
            string += num
            nums.add(int(string))

    count = 0
    for num in nums:
        if is_prime(num):
            count += 1

    return count
