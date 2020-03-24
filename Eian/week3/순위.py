#!/usr/bin/env python3


def solution(n, results):
    win = {i: set() for i in range(1, n+1)
    lose = {i: set() for i in range(1, n+1)

    for winner, loser in results:
        win[winner].add(loser)
        lose[loser].add(winner)

    for i in range(1, n+1):
        for winner in lose[i]:
            win[winner].update(win[i])
        for loser in win[i]:
            lose[loser].update(lose[i])

    count = 0
    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n - 1:
            count += 1
    return count
