from collections import deque


def bfs(computers, visited, start):
    q = deque()
    q.append(start)
    while q:
        node = q.popleft()
        if not visited[node]:
            visited[node] = 1

        for connect_node in range(len(computers)):
            if not visited[connect_node] and computers[node][connect_node]:
                q.append(connect_node)


def solution(n, computers):
    answer = 0
    visited = [0] * n
    while not all(visited):
        for node in range(n):
            if not visited[node]:
                bfs(computers, visited, node)
                answer += 1
    return answer
