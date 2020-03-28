from collections import deque

LOSE, WIN = 0, 1

def solution(n, results):
    def bfs(target):
        q = deque([target])
        visited[i] = True
        
        while q:
            player_a = q.popleft()
            for player_b, result in adj[player_a]:
                if not visited[player_b] and result == WIN:
                    visited[player_b] = True
                    
                    adj[target].add((player_b, WIN))
                    adj[player_b].add((target, LOSE))

                    q.append(player_b)


    adj = [set() for _ in range(n)]

    for a, b in results:
        a -= 1; b -= 1
        adj[a].add((b, WIN))
        adj[b].add((a, LOSE))
        
    for i in range(n):
        visited = [False]*n
        bfs(i)
    
    return sum(1 for i in range(n) if len(adj[i]) == n - 1)
