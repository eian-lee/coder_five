
def solution(citations):
    citations.sort()
    N = len(citations)
    for i,ciation in enumerate(citations):
        if ciation >= N-i:
            return N-i
    return 0