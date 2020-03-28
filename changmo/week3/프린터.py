PRIOR, LOC = 0, 1
def solution(priorities, location):
    N = len(priorities)
    printer = list(zip(priorities, range(N)))
    
    answer = 0
    while True:
        top_prior_loc = printer.index(max(printer, key=lambda x: x[PRIOR]))
        
        answer += 1
        
        doc_order = printer[top_prior_loc][LOC]
        
        if doc_order == location:
            return answer

        printer = printer[top_prior_loc + 1:] + printer[:top_prior_loc]
