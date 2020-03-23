def solution(n, times):
    l, r = 1, max(times) * n
    
    while l <= r:
        m = (l + r) // 2
        
        condition = sum(m // time for time in times)
        
        if condition >= n:
            r = m - 1
        else:
            l = m + 1
    
    return r + 1
