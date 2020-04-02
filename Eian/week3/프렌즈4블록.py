#!/usr/bin/env python3


def transpose(m, n, board):
    return n, m, list(map(list, zip(*board)))

def popitem(m, n, board):
    removed = set()
    for i in range(m-1):
        for j in range(n-1):
            if (board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1] != None):
                removed.update({(i, j), (i, j+1), (i+1, j), (i+1, j+1)})
    return removed

def update(m, n, popped, board):
    for x, y in popped:
        board[x][y] = None
    for i in range(m):
        stack = [board[i][j] for j in range(n) if board[i][j] != None]
        board[i] = [None] * (n-len(stack)) + stack

def solution(m, n, board):
    m, n, board = transpose(m, n, board)
    answer = 0
    while True:
        popped = popitem(m, n, board)
        if len(popped) == 0:
            break
        else:
            answer += len(popped)
            update(m, n, popped, board)
    return answer
