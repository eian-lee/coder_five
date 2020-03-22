def solution(n, computers):
    visited, bfs_node = [False] * n, []
    count = 0
    
    for i in range(n):
        if visited[i]:
            continue       
        count += 1
        bfs_node.append(i)         
        
        while bfs_node:
            index = bfs_node.pop()
            visited[index] = True
            for j, connect in enumerate(computers[index]):
                if connect == 1 and not visited[j]:
                    bfs_node.append(j)
                    
    return count
