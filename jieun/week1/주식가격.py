from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)

    while prices:
        cnt = 0
        value = prices.popleft()
        for i in prices:
            if value > i:
                cnt += 1
                break
            cnt += 1
        answer.append(cnt)
    return answer

