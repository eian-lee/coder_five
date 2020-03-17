import itertools

def solution(baseball):
    num_set = [str(num) for num in range(1, 10)]
    num_set = set(map(''.join, itertools.permutations(num_set, 3)))

    for ball in baseball:
        temp = set()
        for num in num_set:
            ball[0] = str(ball[0])
            s, b = 0, 0
            for i in range(3):
                if num[i] == ball[0][i]:
                    s += 1
                    continue
                if num[i] in ball[0]:
                    b += 1
            if s == ball[1] and b == ball[2]:
                temp.add(num)
        num_set = num_set & temp

    return len(num_set)