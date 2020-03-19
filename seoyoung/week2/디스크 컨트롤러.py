import heapq
def solution(jobs):
    N, REQUEST = len(jobs), 0
    heapq.heapify(jobs)
    jobs_done, curr_time, cand, waits = 0, 0, [], []
    
    while jobs_done < N:
        if not cand:
            request, time = heapq.heappop(jobs)
            curr_time = request + time
            waits.append(time)

        else:
            time, request = heapq.heappop(cand)
            curr_time += time
            waits.append(curr_time - request)

        jobs_done += 1
            
        while jobs and curr_time >= jobs[0][REQUEST]:
            heapq.heappush(cand, heapq.heappop(jobs)[::-1])
            
    return sum(waits) // N
