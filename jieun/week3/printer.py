from collections import deque

def solution(priorities, location):
    p_list = deque(enumerate(priorities))
    priorities.sort(reverse=True)
    idx, VALUE = 0, 1
    done = []

    while True:
        priority = p_list.popleft()
        if not p_list:
            done.append(priority)
            break
        if priorities[idx] == priority[VALUE]:
            done.append(priority)
            idx += 1
        else:
            p_list.append(priority)
    idx_done = [i for i, _ in done]

    return idx_done.index(location) + 1
