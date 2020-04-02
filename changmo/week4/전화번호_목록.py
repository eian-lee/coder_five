def solution(phone_book):
    phone_book = set(phone_book)
    for phone in phone_book:
        for i in range(1, len(phone)):
            if phone[:i] in phone_book:
                return False
    return True