from collections import deque

"""
f_i = from_index
f_c = from_computer
t_i = to_index
is_conn = is_connected
s_i = start_index
"""
def solution(n, computers):
    computers = [[t_i for t_i, is_conn in enumerate(f_c) if is_conn and f_i != t_i] for f_i, f_c in enumerate(computers)]

    answer = 0
    visited = [False]*n
    for s_i in range(n):
        if not visited[s_i]:
            visited[s_i] = True
            answer += 1
            
            q = deque([s_i])
            while q:
                f_i = q.popleft()
                for t_i in computers[f_i]:
                    if not visited[t_i]:
                        visited[t_i] = True
                        q.append(t_i)

    return answer
