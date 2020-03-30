def solution(phone_book):
    cache = set()
    for phone in phone_book:
        for cached_phone in cache:
            if cached_phone == phone[:len(cached_phone)] or phone == cached_phone[:len(phone)]:
                return False
        cache.add(phone)
    return True
