#!/usr/bin/env python3

def compare(guess, number):
    strike, ball = (0, 0)
    for i in range(3):
        if guess[i] == number[i]:
            strike += 1
        elif guess[i] in number:
            ball += 1
    return strike, ball

def status(baseball: list):
    return (
        (str(guess), strike, ball)
        for guess, strike, ball in baseball
    )

def permutations(number: str):
    return (
        number[x] + number[y] + number[z]
        for x in range(9)
        for y in range(9)
        for z in range(9)
        if x != y != z != x # 정수비교에 keyword operand 필요없는듯
    )

def solution(baseball):
    numbers = tuple(map(str, range(1, 10)))
    boards = [number for number in permutations(numbers)]
    for guess, strike, ball in status(baseball):
        boards = [n for n in boards if compare(guess, n) == (strike, ball)]
    return len(boards)
