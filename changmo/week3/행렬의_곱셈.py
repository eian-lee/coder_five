from itertools import product

def solution(arr1, arr2):
    arr2 = list(map(list, zip(*arr2)))
    
    R, C = len(arr1), len(arr2)

    answer = [[0]*C for _ in range(R)]
    for r, c in product(range(R), range(C)):
        answer[r][c] = sum(v1*v2 for v1, v2 in zip(arr1[r], arr2[c]))
    
    return answer
