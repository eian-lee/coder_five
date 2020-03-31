from collections import defaultdict

def solution(n, results):
    answer = 0
    wins = defaultdict(set)
    loses = defaultdict(set)

    for a, b in results:
        wins[a].add(b)
        loses[b].add(a)

    for i in range(n):
        for loser in wins[i + 1]:
            loses[loser].update(loses[i + 1])
        for winner in loses[i + 1]:
            wins[winner].update(wins[i + 1])

    for i in range(n):
        if len(wins[i + 1]) + len(loses[i + 1]) == n - 1:
            answer += 1

    return answer