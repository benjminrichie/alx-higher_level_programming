#!/usr/bin/python3
def roman_to_int(roman_string: str):
    if roman_string is None or type(roman_string) != str:
        return 0
    storage = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    myNum = [storage[x] for x in roman_string] + [0]
    x = 0

    for myItems in range(len(myNum) - 1):
        if myNum[myItems] >= myNum[myItems+1]:
            x += myNum[myItems]
        else:
            x -= myNum[myItems]

    return x
