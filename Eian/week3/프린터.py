#!/usr/bin/env python3


from collections import deque


def solution(priorities, location):
    order = 0
    queue = deque((i, priority) for i, priority in enumerate(priorities))

    while queue:
        index, curr = queue.popleft()

        if any(curr < elem for _, elem in queue):
            queue.append((index, curr))
        else:
            order += 1
            if index == location:
                break
    
    return order
