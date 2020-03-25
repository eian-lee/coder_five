from itertools import permutations


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


def solution(numbers):
    answer = 0
    candidates = list(set(map(int, [''.join(j) for i in range(len(numbers)) for j in permutations(numbers, i + 1)])))
    print(candidates)
    for candidate in candidates:
        answer += is_prime(candidate)
    return answer
