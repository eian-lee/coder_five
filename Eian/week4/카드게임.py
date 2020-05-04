#!/usr/bin/env python3
    
def solution(left, right):
    N = len(left)
    dp = [[0] * (N+1) for _ in range(N+1)]
    
    
    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            if left[i] > right[j]:
                dp[i][j] = dp[i][j+1] + right[j]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i+1][j+1])
            
    return dp[0][0]


if __name__ == "__main__":
            
    print(solution([3,3,1], [7,7,1]))
    print(solution([3,2,5], [2,4,1]))