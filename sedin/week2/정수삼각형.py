def solution(triangle):
    for i in range(1, len(triangle)):
        last_row = len(triangle[i]) - 1
        for j in range(len(triangle[i])):
            child = triangle[i][j]
            left_parent = right_parent = 0
            if not j:
                right_parent = triangle[i - 1][j]
            elif j == last_row:
                left_parent = triangle[i - 1][j - 1]
            else:
                left_parent = triangle[i - 1][j - 1]
                right_parent = triangle[i - 1][j]
            triangle[i][j] = max(left_parent, right_parent) + child
    return max(triangle[-1])
