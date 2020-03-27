from collections import deque
def solution(priorities, location):
    N, PRIOR = len(priorities), 0
    que = deque(zip(priorities,range(N)))
    
    while que:
        if que[0][PRIOR] >= max(que)[PRIOR]:
            prior, init_loc = que.popleft()
            if init_loc == location: return N - len(que)
        else:
            que.append(que.popleft())
