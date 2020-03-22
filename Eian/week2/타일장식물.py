#!/usr/bin/env python3


def solution(N):
    x, y = 0, 1
    for _ in range(N):
        x, y = y, x + y
    return x * 2 + y * 2
