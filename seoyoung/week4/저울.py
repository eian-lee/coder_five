def solution(weight):
    weight.sort()
    nxt = 1
    for w in weight:
        if w > nxt:
            break;
        nxt += w
    return nxt
