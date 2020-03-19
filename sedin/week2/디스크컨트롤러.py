import heapq


def solution(jobs):
    answer = 0
    jobs.sort()
    current_time = jobs[0][0]
    num_jobs = len(jobs)
    heap = []

    while jobs:
        start, process = jobs.pop(0)

        current_time += process
        answer += current_time - start

        while jobs and jobs[0][0] < current_time:
            start, process = jobs.pop(0)
            heapq.heappush(heap, [-process, start])

        while heap:
            process, start = heapq.heappop(heap)
            jobs.insert(0, [start, -process])
    return answer // num_jobs
