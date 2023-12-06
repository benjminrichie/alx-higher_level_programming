#!/usr/bin/python3
def to_subtract(list_num):
    subtract = 0
    _list = max(list_num)

    for n in list_num:
        if _list > n:
            subtract += n

    return (_list - subtract)


def roman_to_int(roman_string):
    if not roman_string:
        return 0
