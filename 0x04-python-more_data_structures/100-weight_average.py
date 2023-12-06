#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    myNum = 0
    x = 0

    for myItems in my_list:
        myNum += myItems[0] * myItems[1]
        x += myItems[1]

    return (myNum / x)
