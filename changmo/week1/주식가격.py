def solution(prices):
    N = len(prices)
    answer = [0]*N

    for i in range(N):
        i_moment_price = prices[i]
        for j in range(i + 1, N):
            j_moment_price = prices[j]

            answer[i] += 1
            if i_moment_price > j_moment_price:
                break

    return answer
