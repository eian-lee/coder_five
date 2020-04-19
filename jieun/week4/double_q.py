import heapq

def solution(operations):
    answer = []
    for cmd in operations:
        if cmd[0] == "I":
            heapq.heappush(answer, int(cmd[2:]))
        else:
            if answer:
                if cmd == "D 1":
                    answer.pop(answer.index(heapq.nlargest(1, answer)[0]))
                else:
                    heapq.heappop(answer)
            else:
                pass

    if not answer:
        return [0, 0]

    return [max(answer), answer[0]]