from itertools import permutations

# 창모님 코드를 참조하여 작성
def solution(baseball):
    answer = 0
    for case in permutations(range(1, 10), 3):
        for number, strike, ball in baseball:
            s_cnt, b_cnt, number = 0, 0, str(number)
            # zip과 str을 활용하여, 인덱스 접근 없이 비교
            for trial, target in zip(case, number):
                if trial == int(target):
                    s_cnt += 1
                elif str(trial) in number:
                    b_cnt += 1

            if s_cnt != strike or b_cnt != ball:
                break
        else:
            answer += 1

    return answer
