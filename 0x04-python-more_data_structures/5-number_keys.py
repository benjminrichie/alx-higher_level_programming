#!/usr/bin/python3
def number_keys(a_dictionary):
    myNum = 0
    list_keys = list(a_dictionary.keys())

    for items in list_keys:
        myNum += 1

    return (myNum)
