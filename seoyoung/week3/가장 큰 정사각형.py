import itertools

def solution(board):
    M, N = len(board), len(board[0])
    for i in range(1, M):
        for j in range(1, N):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1

    return max(itertools.chain(*board))**2

''' 풀이 1 -> itertoolss.chain ->2차배열을 1차배열로 (시간초과)

import itertools

def solution(board):
    M, N = len(board), len(board[0])
    MAX = max(M, N)
    
    for l in range(MAX, 0, -1):
        for m in range(M-l+1):
            for n in range(N-l+1):
                cand = [row[n:l+n]for row in board[m:l+m]]
                if all(itertools.chain(*cand)):
                    return l*l
    return 0
'''

''' 풀이 2 -> 0 발견 시 브레이크 (시간초과)

def solution(board):
    M, N = len(board), len(board[0])
    MAX = max(M, N)
    for l in range(MAX, 0, -1):
        for m in range(M-l+1):
            for n in range(N-l+1):
                for row in board[m:l+m]:
                    if not all(row[n:l+n]): break;
                else: return l*l
    return 0
'''
