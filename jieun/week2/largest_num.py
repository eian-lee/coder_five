def solution(number, k):
    answer = []

    for idx, num in enumerate(number):
        while answer and k > 0 and num > answer[-1]:
            answer.pop()
            k -= 1

        if k == 0:
            answer.extend(number[idx:])
            break
        answer.append(num)

    answer = answer[:-k] if k > 0 else answer
    return ''.join(answer)