#!/usr/bin/env python3

import heapq

def solution(operations):
    queue = []
    answer = []
    for operation in operations:
        cmd, num = operation.split(" ")
        if cmd == "I":
            heapq.heappush(queue, int(num))
        elif queue:
            if num == "1":
                queue.pop()
            if num == "-1":
                heapq.heappop(queue)
    if queue:
        answer.append(max(queue))
        answer.append(heapq.heappop(queue))
    return answer if answer else [0, 0]
    

