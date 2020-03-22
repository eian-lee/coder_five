#!/usr/bin/env python3


from itertools import islice
from operator import itemgetter
from collections import defaultdict


def _sorted(elem):
    return sorted(elem, key=itemgetter(1), reverse=True)

def solution(genres, plays):
    chart = {}
    counts = defaultdict(int)

    for index, value in enumerate(zip(genres, plays)):
        name, count = value
        chart.setdefault(name, []).append((index, value))
        counts[name] += count

    answer = []
    orders = _sorted(counts.items())

    for name, _ in orders:
        albums = _sorted(chart[name])
        answer.append(albums[0][0])
        if len(albums) > 1:
            answer.append(albums[0][0])

    return answer
