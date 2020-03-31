def hanoi(n, f_pos, b_pos, t_pos, answer):
    if n == 1:
        return answer.append([f_pos, t_pos])
    hanoi(n-1, f_pos, t_pos, b_pos, answer)
    answer.append([f_pos, t_pos])
    hanoi(n-1, b_pos, f_pos, t_pos, answer)

def solution(n):
    answer = []
    hanoi(n, 1, 2, 3, answer)
    return answer
