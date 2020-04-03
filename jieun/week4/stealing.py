def solution(money):
    n = len(money)
    temp1 = [0 for _ in range(n - 1)]
    temp2 = [0 for _ in range(n - 1)]
    temp1[0], temp1[1] = money[0], max(money[0], money[1])
    temp2[0], temp2[1] = money[1], max(money[1], money[2])
    for i in range(2, n - 1):
        temp1[i] = max(money[i] + temp1[i - 2], temp1[i - 1])
        temp2[i] = max(money[i + 1] + temp2[i - 2], temp2[i - 1])
    return max(temp1[n - 2], temp2[n - 2])