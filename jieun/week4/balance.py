def solution(weight):
    answer = 0
    weight.sort()

    for temp in weight:
        if answer + 1 < temp:
            return answer + 1
        answer += temp

    return answer + 1