from itertools import product

def solution(numbers, target):
    
    items = [(num, -num) for num in numbers]
    sums =[True for nums in product(*items) if sum(nums) == target]
        
    return len(sums)