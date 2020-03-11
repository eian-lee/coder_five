#!/usr/bin/env python3


from collections import Counter


def solution(clothes):
    answer = 1
    closet = Counter(ctype for name, ctype in clothes)

    for number in closet.values():
        answer *= (number + 1)

    return answer - 1
