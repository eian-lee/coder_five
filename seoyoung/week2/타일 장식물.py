def solution(N):
    fibo1, fibo2 = 0, 1
    for i in range(N):
        fibo1, fibo2 = fibo2, fibo1 + fibo2
    return fibo1 * 2 + fibo2 * 2

