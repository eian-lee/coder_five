import heapq
from collections import deque

def solution(stock, dates, supplies, k):
    count, plan = 0, []
    dates, supplies = deque(dates), deque(supplies)
    
    while stock < k :
        while dates and dates[0] <= stock:
            dates.popleft()
            heapq.heappush(plan,-supplies.popleft())

        count += 1
        stock += -heapq.heappop(plan)
        
    return count

