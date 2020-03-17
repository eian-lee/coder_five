def solution(numbers, target):
    root = [0]
    for num in numbers:
        temp = []
        for ele in root:
            temp.append(ele + num)
            temp.append(ele - num)
        root = temp

    return root.count(target)