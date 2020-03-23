"""
>>> Brute Force

from itertools import product

def solution(board):
    R, C = len(board), len(board[0])
    
    result = 0
    
    for r, c in product(range(R), range(C)):
        if board[r][c]:
            max_dist = min(R - r, C - c)
            for dist in range(max_dist, 0, -1):
                if dist <= result:
                    break
                
                for rr, cc in product(range(r, r + dist), range(c, c + dist)):
                    if not board[rr][cc]:
                        break
                else:
                    result = dist
    
    return result ** 2
"""

"""
>>> Binary Search

from itertools import product

def solution(board):
    R, C = len(board), len(board[0])
    
    left, right = 1, min(R, C)
    while left <= right:
        mid = (left + right) // 2
        
        flag = False
        for r, c in product(range(R - mid + 1), range(C - mid + 1)):
            if board[r][c]:
                for rr, cc in product(range(r, r + mid), range(c, c + mid)):
                    if not board[rr][cc]:
                        break
                else:
                    flag = True
                    break
        
        if flag:
            left = mid + 1
        else:
            right = mid - 1

    return (left - 1)**2
"""

from itertools import product

def solution(board):
    R, C = len(board), len(board[0])
    
    result = 0
    for r, c in product(range(R), range(C)):
        if r == 0 or c == 0:
            if board[r][c] and not result:
                result = 1
            continue

        if board[r][c]:
            target = [board[rr][cc] for rr, cc in product([r - 1, r], [c - 1, c])]
            board[r][c] += min(target[:-1])
            if board[r][c] > result:
                result = board[r][c]

    return result ** 2
