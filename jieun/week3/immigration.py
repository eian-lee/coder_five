def solution(n, times):
    times = sorted(times)
    left, right = 1, times[-1] * n

    while left < right:
        mid = (left + right) // 2
        temp = 0
        for i in range(len(times)):
            temp += mid // times[i]
        if temp >= n:
            right = mid
        else:
            left = mid + 1

    return right