from itertools import permutations

def solution(numbers):
    max_num = int(''.join(sorted(list(numbers), reverse=True)))
    prime_set = set(range(2, max_num + 1))
    for i in range(2, max_num + 1):
        if i in prime_set:
            prime_set -= set(range(i * 2, max_num + 1, i))

    answer = 0
    for i in range(len(numbers)):
        for subset in permutations(numbers, i + 1):
            num = int(''.join(subset))
            if num in prime_set:
                answer += 1
                prime_set.remove(num)

    return answer