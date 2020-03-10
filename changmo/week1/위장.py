from collections import defaultdict

def solution(clothes):
    clothes_count_by_kind = defaultdict(int)
    
    for _, kind in clothes:
        clothes_count_by_kind[kind] += 1
    
    pieces = [count + 1 for count in clothes_count_by_kind.values()]

    return eval("*".join(str(piece) for piece in pieces)) - 1
