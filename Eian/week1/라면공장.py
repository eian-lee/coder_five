#!/usr/bin/env python3


import heapq
from collections import deque


def solution(stock, dates, supplies, k):
    answer = 0
    ledger = deque(zip(dates, supplies))

    heap = []
    while stock < k:
        while ledger and ledger[0][0] <= stock:
            heapq.heappush(heap, -ledger.popleft()[1])
        answer += 1
        stock += -heapq.heappop(heap)
    
    return answer

if __name__ == "__main__":
    stock = 4
    dates = [4, 10, 15]
    supplies = [20, 5, 10]
    k = 30

    print(solution(stock, dates, supplies, k))
