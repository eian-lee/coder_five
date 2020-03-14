# kick1212 님것 보고 따라 쳤어요.

from collections import deque
import heapq

def solution(stock, dates, supplies, k):
    pairs = []
    for i in range(len(dates)):
        pairs.append((dates[i], supplies[i]))
    pairs = deque(pairs)
    DATE, SUPPLY = 0, 1

    q = []
    answer = 0

    while stock < k:
        while pairs and pairs[0][DATE] <= stock:
            pair = pairs.popleft()
            heapq.heappush(q, -pair[SUPPLY])

        amount = heapq.heappop(q)
        stock += -amount
        answer += 1

    return  answer

