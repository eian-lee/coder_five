# 테스트 케이스 16번 통과 x

def solution(left, right):
    L, R = len(left), len(right)
    score = [[0] * (L+1) for j in range(R+1)]
    for i in range(1, L+1):
        for j in range(1, R+1):
            if left[i-1] > right[j-1]: 
                score[i][j] = score[i][j-1] + right[j-1]
            else: 
                score[i][j] = max(score[i-1][j-1], score[i-1][j])

    return score[L][R]

