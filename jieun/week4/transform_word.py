def comparison(str1, str2):
    answer = 0
    for ele1, ele2 in zip(str1, str2):
        if ele1 == ele2:
            answer += 1
    if answer == len(str1) - 1:
        return True

    return False

def solution(begin, target, words):
    if target not in words:
        return 0

    graph = dict()
    graph[0] = [begin]
    for i in range(1, len(words)):
        temp = []
        for comp in graph[i - 1]:
            for word in words:
                if comparison(comp, word):
                    temp.append(word)

        if target in temp:
            return i
        graph[i] = temp

