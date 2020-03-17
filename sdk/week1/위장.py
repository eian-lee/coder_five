from collections import Counter
from functools import reduce

def solution(clothes):
    cnt = Counter([kind for name, kind in clothes])

    print cnt.values()

    return reduce(lambda x, y:x*(y+1), cnt.values(), 1) -1

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])
