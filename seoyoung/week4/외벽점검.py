def solution(n, weak, dist):
    
    W, F = len(weak), len(dist)
    repair_lst = [()]
    count = 0
    
    for can_move in dist[::-1]:
        repairs = []
        count += 1
        
        for i, wp in enumerate(weak):
            start = wp
            ends = weak[i:] + [n+w for w in weak[:i]]
            can = [end % n for end in ends if end - start <= can_move]
            repairs.append(set(can))
            
        cand = set()
        for r in repairs: 
            for x in repair_lst: 
                new = r | set(x)
                if len(new) == W:
                    return count
                cand.add(tuple(new))
        repair_lst = cand
        
    return -1
