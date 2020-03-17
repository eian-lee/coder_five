def solution(citations):
    citations.sort()
    N = len(citations)
    for i in range(N):
        if citations[i] >= N-i:
            return N-i
    return 0
