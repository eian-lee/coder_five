from collections import Counter

def solution(clothes):
    kinda_clothes = [ele[1] for ele in clothes]
    my_dict = dict(Counter(kinda_clothes))

    answer = 1
    cnt_list = list(my_dict.values())
    for cnt in cnt_list:
        answer *= (cnt + 1)
    return answer - 1