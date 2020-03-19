#!/usr/bin/env python3

from itertools import product

def solution(numbers, target):
    numbers = [(n, -n) for n in numbers]
    return list(map(sum, product(*numbers))).count(target)
