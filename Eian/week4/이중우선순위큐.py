#!/usr/bin/env python3

from heapq import heapify, heappop, heappush

def solution(operations):
    queue = []
    answer = []
    for operation in operations:
        cmd, num = operation.split(" ")
        if cmd == "I":
            heappush(queue, int(num))
        elif queue:
            if num == "1":
                queue.pop()
            if num == "-1":
                heappop(queue)
    if queue:
        answer.append(max(queue))
        answer.append(heappop(queue))
    return answer if answer else [0, 0]
    

