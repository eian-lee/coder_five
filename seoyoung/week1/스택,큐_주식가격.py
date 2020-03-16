from collections import deque

def solution(prices):
    count = []
    prices = deque(prices)
    
    while prices:
        current, time = prices.popleft(), 0
        for price in prices:
            time += 1
            if current > price:
                break

        count.append(time)

    return count