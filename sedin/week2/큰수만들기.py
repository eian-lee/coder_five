def solution(number, k):
    stack = []

    for i, num in enumerate(number):
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1

        if k == 0:
            stack += number[i:]
            break

        stack.append(num)

    stack = stack[:-k] if k > 0 else stack
    return "".join(stack)
