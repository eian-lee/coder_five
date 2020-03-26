def dfs(computers, visited, start):
    stack = [start]
    while stack:
        j = stack.pop()
        if visited[j] == 0:
            visited[j] = 1
        for i in range(len(computers)):
            if computers[j][i] == 1 and visited[i] == 0:
                stack.append(i)

def solution(n, computers):
    cnt = 0
    visited = [0 for _ in range(n)]

    for i in range(n):
        if visited[i] == 0:
            dfs(computers, visited, i)
            cnt += 1

    return cnt