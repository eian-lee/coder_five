def solution(stock, dates, supplies, k):
    import heapq as hq
    answer = 0
    heap = []
    idx = 0

    while stock < k:
        for i in range(idx, len(dates)):
            if dates[i] <= stock:
                hq.heappush(heap, (-supplies[i], supplies[i]))
                idx = i + 1
            else:
                break
        stock += hq.heappop(heap)[1]
        answer += 1
    return answer
