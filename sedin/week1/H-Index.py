def solution(citations):
    for idx, citation in enumerate(sorted(citations)):
        if citation >= len(citations) - idx:
            return len(citations) - idx
    return 0
