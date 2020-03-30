import heapq

METHOD, NUM = 0, 1
MIN, MAX = 0, 1
def solution(operations):
    double_priority_q = [[] for _ in range(2)]
    
    insert, delete = 0, 0
    for op in operations:
        op = op.split()
        if op[METHOD] == 'I':
            op[NUM] = int(op[NUM])
            heapq.heappush(double_priority_q[MIN], op[NUM])
            heapq.heappush(double_priority_q[MAX], -op[NUM])
            insert += 1
        elif op[NUM] == '1' and double_priority_q[MAX]:
            heapq.heappop(double_priority_q[MAX])
            delete += 1
        elif op[NUM] == '-1' and double_priority_q[MIN]:
            heapq.heappop(double_priority_q[MIN])
            delete += 1

        if insert == delete:
            double_priority_q = [[] for _ in range(2)]

    if insert == delete:
        return [0, 0]
    else:
        return [-heapq.heappop(double_priority_q[MAX]), heapq.heappop(double_priority_q[MIN])]
