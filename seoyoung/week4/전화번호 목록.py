import re

def solution(phone_book):
    
    for pre in phone_book:
        for number in phone_book:
            if re.search("^"+pre+".+",number):
                return False
                    
    return True
