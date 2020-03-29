def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    
    for i, r in enumerate(arr1):
        for j, c in enumerate(zip(*arr2)):
            answer[i][j] = sum([x*y for x,y in zip(r,c)])
    return answer

''' numpy사용 - 훨씬 빠름
import numpy as np 
def solution(arr1, arr2):
    return (np.matrix(arr1)*np.matrix(arr2)).tolist()
'''
