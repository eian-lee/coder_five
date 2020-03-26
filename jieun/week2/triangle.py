def solution(triangle):
    for i in range(len(triangle) - 1):
        array1 = triangle[-1]
        array2 = triangle[-2]
        for j in range(len(array2)):
            array2[j] += max(array1[j], array1[j + 1])
        triangle.pop()
        triangle[-1] = array2

    return triangle[0][0]