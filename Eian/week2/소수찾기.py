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
    """
    테스트 1 〉 통과 (0.11ms, 10.9MB)
    테스트 2 〉 통과 (2.60ms, 11MB)
    테스트 3 〉 통과 (0.06ms, 10.9MB)
    테스트 4 〉 통과 (1.14ms, 10.9MB)
    테스트 5 〉 통과 (8.57ms, 11MB)
    테스트 6 〉 통과 (0.06ms, 10.9MB)
    테스트 7 〉 통과 (0.11ms, 10.8MB)
    테스트 8 〉 통과 (8.69ms, 10.9MB)
    테스트 9 〉 통과 (0.10ms, 10.9MB)
    """
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
