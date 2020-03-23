def solution(triangle):
    N = len(triangle)
    dp = [[0]*(w + 1) for w in range(N)]
    dp[0][0] = triangle[0][0]

    for r in range(1, N):
        for c in range(len(dp[r])):
            if c - 1 >= 0:
                target = dp[r - 1][c - 1] + triangle[r][c]
                if target > dp[r][c]:
                    dp[r][c] = target
                    
            if c < len(dp[r - 1]):
                target = dp[r - 1][c] + triangle[r][c]
                if target > dp[r][c]:
                    dp[r][c] = target

    return max(dp[-1])
