#!/usr/bin/env python3


from collections import deque

def replaceable(*args):
    return sum(x != y for x, y in zip(*args)) == 1

def solution(begin, target, words):
    queue = deque([(begin, 0)])
    visited = set()
    
    while queue:
        curr, depth = queue.popleft()
        for word in words:
            if replaceable(curr, word) and word not in visited:
                if word == target:
                    return depth + 1
                
                visited.add(word)
                queue.append((word, depth+1))
    return 0


if __name__ == "__main__":
    print(solution("hit", "cog", ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
