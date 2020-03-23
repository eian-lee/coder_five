def solution(priorities, location):
    N = len(priorities)
    order = list(range(N))
    
    answer = 0
    while True:
        top_pri_loc = priorities.index(max(priorities))
        
        answer += 1
        
        doc_order = order[top_pri_loc]
        
        if location == doc_order:
            return answer

        priorities = priorities[top_pri_loc + 1:] + priorities[:top_pri_loc]
        order = order[top_pri_loc + 1:] + order[:top_pri_loc]
