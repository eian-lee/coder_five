def solution(numbers, target):
    def check(index, sub_result):
        nonlocal answer
        if index == len(numbers):
            if sub_result == target:
                answer += 1
            return
    
        check(index + 1, sub_result + numbers[index])
        check(index + 1, sub_result - numbers[index])


    answer = 0
    check(0, 0)
    return answer
