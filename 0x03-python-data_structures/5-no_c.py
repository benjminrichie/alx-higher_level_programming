#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for q in my_string:
        if (q != 'c') and (q != 'C'):
            new_str += q
    return (new_str)
