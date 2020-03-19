import heapq

def solution(jobs):
    cur, spent_time, poss_jobs = 0, [], []
    heapq.heapify(jobs)

    while jobs:
        while jobs and jobs[0][0] < cur + 1:
            poss_jobs.append(heapq.heappop(jobs))

        if poss_jobs:
            poss_jobs.sort(key=lambda x: x[1], reverse=True)
            work = poss_jobs.pop()
            cur += work[1]
            spent_time.append(cur - work[0])
        else:
            cur += 1

    while poss_jobs:
        work = poss_jobs.pop()
        cur += work[1]
        spent_time.append(cur - work[0])

    answer = sum(spent_time) // len(spent_time)
    return answer