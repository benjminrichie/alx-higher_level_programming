#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_ord = list(a_dictionary.keys())
    list_ord.sort()
    for myItems in list_ord:
        print("{}: {}".format(myItems, a_dictionary.get(myItems)))
