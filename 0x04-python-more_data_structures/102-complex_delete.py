#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    _keys = list(a_dictionary.keys())

    for theItems in _keys:
        if value == a_dictionary.get(theItems):
            del a_dictionary[theItems]

    return (a_dictionary)
