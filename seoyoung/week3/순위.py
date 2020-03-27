def solution(n, results):
    chart = [[0] * n for _ in range(n)] 
    WIN, LOSE = 1, -1
    for i, j in results:
        chart[i-1][j-1], chart[j-1][i-1] = WIN, LOSE

    for me in range(n): 
        wins = [opp for opp, x in enumerate(chart[me]) if x == WIN]
        while wins:
            win = wins.pop()
            for opp, x in enumerate(chart[win]):
                if x == WIN and chart[me][opp] == 0:
                    chart[me][opp], chart[opp][me] = WIN, LOSE
                    wins.append(opp)

    return len(['know' for x in chart if x.count(0) == 1])
