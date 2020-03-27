def solution(board):
    R = len(board)
    C = len(board[0])
    array = [[0 for _ in range(C)] for _ in range(R)]
    array[0] = board[0]
    for i in range(R):
        array[i][0] = board[i][0]

    for i in range(1, R):
        for j in range(1, C):
            if board[i][j] == 1:
                array[i][j] = min(array[i][j - 1], array[i - 1][j], array[i - 1][j - 1]) + 1
            else:
                array[i][j] = 0
    answer = max(max(x) for x in array)

    return answer ** 2