def solution(arr1, arr2):
    M, N = len(arr1), len(arr1[0])
    N, K = len(arr2), len(arr2[0])
    answer = [[0] * K for _ in range(M)]

    for i in range(M):
        for j in range(K):
            row = arr1[i]
            col = [arr2[k][j] for k in range(N)]
            answer[i][j] = sum(a*b for a, b in zip(row, col))
            
    return answer
