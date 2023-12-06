#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    myNum = 0

    for items in uniq_list:
        myNum += items

    return (myNum)
