'''
numbers = [1, 1, 1], target = 2일 때 트리 구조
depth 0:                            0
depth 1:                +1                  -1
depth 2:          +1          -1       +1         -1
depth 3:        +1  -1      +1  -1  +1  -1      +1  -1
depth가 len numbers와 같아 질 때, 합이 target과 같은가?
'''


def dfs(numbers, target, length, depth=0):
    answer = 0
    if depth == len(numbers):
        if sum(numbers) == target:
            return 1
    else:
        answer += dfs(numbers, target, length, depth + 1)
        numbers[depth] *= -1
        answer += dfs(numbers, target, length, depth + 1)
    return answer


def solution(numbers, target):
    return dfs(numbers, target, len(numbers))
