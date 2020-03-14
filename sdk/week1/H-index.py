# eian님것 컨닝
def solution(citations):
    PAPER = len(citations)
    for idx, citation in enumerate(sorted(citations)):
        if citation >= PAPER - idx:
            return PAPER - idx
    return 0



