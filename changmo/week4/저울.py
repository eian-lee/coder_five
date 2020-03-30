def solution(weight):
    weight.sort()
    scale = 0
    for w in weight:
        if w > scale + 1:
            break
        
        scale += w

    return scale + 1
