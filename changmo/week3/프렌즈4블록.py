from itertools import product

DESTROYED = '0'
def solution(R, C, board):
    def search_target():
        for r, c in product(range(R - 1), range(C - 1)):
            if board[r][c] != DESTROYED:
                for rr, cc in product(range(r, r + 2), range(c, c + 2)):
                    if board[rr][cc] != board[r][c]:
                        break
                else:
                    add_target_to_destroy_set(r, c)


    def add_target_to_destroy_set(r, c):
        for rr, cc in product(range(r, r + 2), range(c, c + 2)):
            destroy_set.add((rr, cc))


    def destroy_target():
        nonlocal answer
        answer += len(destroy_set)
        for r, c in destroy_set:
            board[r][c] = DESTROYED
        destroy_set.clear()

    
    def clear_board():
        nonlocal board
        
        board = list(map(list, zip(*board)))
        
        for c in range(C):
            board[c] = [elem for elem in board[c] if elem != DESTROYED]
            board[c] = [DESTROYED] * (R - len(board[c])) + board[c]
        
        board = list(map(list, zip(*board)))
        

    board = [list(board[i]) for i in range(R)]
    
    answer = 0
    destroy_set = set()
    while True:
        search_target()
        
        if not destroy_set:
            return answer
        
        destroy_target()
        
        clear_board()
