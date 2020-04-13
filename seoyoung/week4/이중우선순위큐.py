from collections import deque
def solution(operations):
    MIN = -1
    operations = [(op[0], int(op[2:]))for op in operations]
    que = deque([])

    for command, num in operations:
        if command == 'I':
            for i in range(len(que)):
                if que[i] >= num:
                    que.insert(i, num)
                    break
            else:
                que.append(num)
                
        elif que:
            if num == MIN: 
                que.popleft()
            else: 
                que.pop()

    return [que.pop(), que.popleft()] if que else [0, 0]
