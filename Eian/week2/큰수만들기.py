#!/usr/bin/env python


def solution(number, k):
    stack = []
    for i, _ in enumerate(number):
        while stack and k > 0 and stack[-1] < number[i]:
            stack.pop()
            k -= 1
        stack.append(number[i])
    return "".join(stack[:len(stack) - k])
