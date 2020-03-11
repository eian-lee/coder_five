#!/usr/bin/env python3


def solution(prices):
    N = len(prices)
    ticker = [0] * N

    stack = []
    for i in range(N):
        while stack and prices[stack[-1]] > prices[i]:
            close = stack.pop()
            ticker[close] = i - head
        stack.append(i)
    
    while stack:
        close = stack.pop()
        answer[close] = N - 1 - close
    
    return answer
