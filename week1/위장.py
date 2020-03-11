from collections import Counter
from functools import reduce
from operator import mul


def solution(clothes):
    number_of_item = [num + 1 for num in Counter((dict(clothes).values())).values()]
    print(number_of_item)
    return reduce(mul, number_of_item) - 1
