def hanoi(num, fr, to, temp, moves):
    if num == 1:
        moves.append([fr,to])
    else:
        hanoi(num-1, fr, temp, to, moves)
        moves.append([fr,to])
        hanoi(num-1, temp, to, fr, moves)
    
def solution(n):
    moves = []
    hanoi(n, 1, 3, 2, moves)
    return moves
