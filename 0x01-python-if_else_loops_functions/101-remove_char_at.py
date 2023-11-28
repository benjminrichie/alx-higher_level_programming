#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""
    w = 0
    for c in str:
        if w != n:
            new += c
        w += 1
    return new
