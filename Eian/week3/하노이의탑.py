#!/usr/bin/env python3



def solution(n):
    def hanoi(m, s, b, d):
        if m == 1:
            yield [s, d]
        else:
            yield from hanoi(m-1, s, d, b)
            yield [s, d]
            yield from hanoi(m-1, b, s, d)

    answer = list(hanoi(n, 1, 2, 3))
    return answer
