def solution(N):
    a, b = 0, 1
    for i in range(N):
        a, b = b, a + b
    return 2 * (a + b)
