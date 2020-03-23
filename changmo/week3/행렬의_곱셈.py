def solution(arr1, arr2):
    arr2 = list(map(list, zip(*arr2)))
    
    R, C = len(arr1), len(arr2)

    answer = [[0]*C for _ in range(R)]    
    for r in range(R):
        for c in range(C):
            answer[r][c] = sum(v1*v2 for v1, v2 in zip(arr1[r], arr2[c]))
    
    return answer
