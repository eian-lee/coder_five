dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
ROW, COL = 0, 1
def solution(board):
    N = len(board)
    visited = set()
    
    q = [ ((0, 0), (0, 1))]
    visited.add( ((0, 0), (0, 1)) )
    
    time = 0
    while q:
        qs, q = q, []
        
        for left, right in qs:
            left_r, left_c = left
            right_r, right_c = right
            
            if (left_r, left_c) == (N - 1, N - 1) or (right_r, right_c) == (N - 1, N - 1):
                return time

            if left[ROW] == right[ROW]:
                for x in range(4):
                    new_left_r, new_left_c, new_right_r, new_right_c = left_r + dr[x], left_c + dc[x], right_r + dr[x], right_c + dc[x]
                    if 0 <= new_left_r < N and 0 <= new_left_c < N and 0 <= new_right_r < N and 0 <= new_right_c < N and \
                        not board[new_left_r][new_left_c] and not board[new_right_r][new_right_c] and ((new_left_r, new_left_c), (new_right_r, new_right_c)) not in visited:
                        if x == 0:
                            if ((left_r - 1, left_c + 1), (right_r, right_c)) not in visited:
                                q.append( ((left_r - 1, left_c + 1), (right_r, right_c)) )
                                visited.add( ((left_r - 1, left_c + 1), (right_r, right_c)) )

                            if ((right_r - 1, right_c - 1), (left_r, left_c)) not in visited:
                                q.append( ((right_r - 1, right_c - 1), (left_r, left_c)) )
                                visited.add( ((right_r - 1, right_c - 1), (left_r, left_c)) )

                        elif x == 1:
                            if ((right_r, right_c), (left_r + 1, left_c + 1)) not in visited:
                                q.append( ((right_r, right_c), (left_r + 1, left_c + 1)) )
                                visited.add( ((right_r, right_c), (left_r + 1, left_c + 1)) )
                                
                            if ((left_r, left_c), (right_r + 1, right_c - 1)) not in visited:
                                q.append( ((left_r, left_c), (right_r + 1, right_c - 1)) )
                                visited.add( ((left_r, left_c), (right_r + 1, right_c - 1)) )

                        q.append( ((new_left_r, new_left_c), (new_right_r, new_right_c)) )
                        visited.add( ((new_left_r, new_left_c), (new_right_r, new_right_c)) )
            else:
                for x in range(4):
                    new_left_r, new_left_c, new_right_r, new_right_c = left_r + dr[x], left_c + dc[x], right_r + dr[x], right_c + dc[x]
                    if 0 <= new_left_r < N and 0 <= new_left_c < N and 0 <= new_right_r < N and 0 <= new_right_c < N and \
                        not board[new_left_r][new_left_c] and not board[new_right_r][new_right_c] and ((new_left_r, new_left_c), (new_right_r, new_right_c)) not in visited:
                        if x == 2:
                            if ((left_r + 1, left_c - 1), (right_r, right_c)) not in visited:
                                q.append( ((left_r + 1, left_c - 1), (right_r, right_c)) )
                                visited.add( ((left_r + 1, left_c - 1), (right_r, right_c)) )
                                
                            if ((right_r - 1, right_c - 1), (left_r, left_c)) not in visited:
                                q.append( ((right_r - 1, right_c - 1), (left_r, left_c)) )
                                visited.add( ((right_r - 1, right_c - 1), (left_r, left_c)) )
                                
                        elif x == 3:
                            if ((right_r, right_c), (left_r + 1, left_c + 1)) not in visited:
                                q.append( ((right_r, right_c), (left_r + 1, left_c + 1)) )
                                visited.add( ((right_r, right_c), (left_r + 1, left_c + 1)) )
                                
                            if ((left_r, left_c), (right_r - 1, right_c + 1)) not in visited:
                                q.append( ((left_r, left_c), (right_r - 1, right_c + 1)) )
                                visited.add( ((left_r, left_c), (right_r - 1, right_c + 1)) )
                        
                        q.append( ((new_left_r, new_left_c), (new_right_r, new_right_c)) )
                        visited.add( ((new_left_r, new_left_c), (new_right_r, new_right_c)) )

        time += 1