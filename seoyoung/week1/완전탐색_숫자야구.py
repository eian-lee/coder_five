import itertools
from collections import deque
def solution(baseball):
    cand = deque(itertools.permutations(range(1,10), 3))
    answer = 0
    
    while cand:
        cand_num = cand.popleft()
        
        for num, strike, ball in baseball:
            num = [int(c) for c in str(num)]
            s_count, b_count = 0, 0
            
            for i in range(3):
                if num[i] in cand_num:
                    if num[i] == cand_num[i]:
                        s_count += 1
                    else:
                        b_count += 1
                        
            if strike != s_count or ball != b_count:
                break
        else:
            answer += 1
                
    return answer