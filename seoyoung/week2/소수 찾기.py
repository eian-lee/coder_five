from itertools import permutations
def solution(numbers):
    L = len(numbers)
    N, cand, primes = int('9' * L), set(), set()
    
    prime_check = [False,False] + [True]*(N-1)
    for i in range(2, N+1):
        if prime_check[i]:
            primes.add(i)
            prime_check[i*2::i] = [False] * len(prime_check[i*2::i])
    
    for n in range(L):
        for x in permutations(numbers, n+1):
            number = int(''.join(x))
            if number in primes:
                cand.add(number)
            
    return len(cand)
