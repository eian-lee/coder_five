#!/usr/bin/env python3


def solution(weight):
    answer = 1
    for w in sorted(weight):
        if w <= answer:
            answer += w
    return answer
