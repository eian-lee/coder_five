def solution(n):
    def hanoi(N, f = 1, v = 2, t = 3):
        if N == 1:
            answer.append([f, t])
            return
        
        hanoi(N - 1, f, t, v)
        answer.append([f, t])
        hanoi(N - 1, v, f, t)


    answer = []
    hanoi(n)

    return answer
